# Storm Helpers

## One idea
On the calm, sunny morning after a big storm, the child walks Willow Street stop by stop and hears how the storm changed each neighbor's day in a different way (Mr. Diaz has no power and his fridge is getting warm, the school bus can't cross a flooded road, the school is closed, Mrs. Abbott can't get her car out), then meets the people already helping at three distances (neighbors on the street, power line crews from the next state, crews and a supply truck from much farther away), picks one thing a kid can really do, sees what it does, and makes a poster that says why it helps, so a second grader learns how a disaster affects a place and that people near and far help, and so can they.

## Not like
- community-helpers-village (1, spec): everyday helpers and what a town needs. Here a disaster and help from near and far.
- changemaker-cards (2, spec): people across history. Here one morning on one street.
- town-council (2, spec): a meeting about a lot. Here helping after a storm.
- three-towns (2, spec, this batch): kinds of communities. Here one community after a storm.

## Who and how
- Grade 2, Social Studies (Geography and Taking Action), module "Storm Helpers". Standards: D2.Geo.12.K-2 (identify ways that a catastrophic disaster may affect people living in a place), D4.6.K-2 (identify and explain a range of local, regional, and global problems, and some ways in which people are trying to address these problems), D4.7.K-2 (identify ways to take action to help address local, regional, and global problems), D4.3.K-2 (present a summary of an argument using print, oral, and digital technologies).
- Driver: teacher on the projector with the class, or one child alone; every line, card and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Four parts: Walk the street, Who is helping, How I can help, My poster. tool.json `modes: ["Walk", "Helpers", "I can help", "Poster"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.
- Teacher note (in the teacher panel): some children have lived through storms, floods or power cuts. The tool shows only the calm morning after, with no wind, rain, injuries or damaged homes shown up close. If a child shares a hard memory, the class can pause on the Helpers part, which ends on people keeping each other safe.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.12.K-2 | Visit four stops and match each to how the storm changed that person's day: no power, can't travel, can't go to school, stuck at home | the stop's picture and its "what changed" card (icon plus words) | 2 |
| D4.6.K-2 | Sort the helpers you meet by how far they came: On our street, From the next state, From far away | the three rings around Willow Street filling with helpers | 3 |
| D4.7.K-2 | Pick one kid-sized way to help and watch what it does | the action card and its result scene | 4 |
| D4.3.K-2 | Build a poster: a picture, a reason, and a "You can help too" line, and read it aloud | the poster and its spoken read | 5 |

## Screens and modes
Header (kit): title "Storm Helpers"; `Walk`, `Helpers`, `I can help`, `Poster`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** Willow Street on a bright morning. Branches lie on lawns and a puddle shines on the road; the sky is blue. A dotted path leads to four houses. The welcome is queued (`welcomeAfter: true`): "Last night a big storm blew through. This morning it's calm and sunny. Let's walk down Willow Street and see how everyone is doing. Tap the first house." First hint: "Tap the first house." The first tap starts stop 1 and cuts the welcome.

**Walk (focus: the current stop).** At 1366x768 the street map is at the left with a dot for each stop, the stop scene is center, and four "what changed" cards sit at the right: No power (a plug), Can't travel (a road sign), No school (a closed book), Stuck at home (a house). At 680x425 the map hides behind a `Map` button.
- Stop 1, Mr. Diaz: "The power went out in the storm. My fridge is getting warm, so I have to throw out my milk. And no lights tonight." Card: No power.
- Stop 2, Ms. Kaye the bus driver at the corner: "The road by the creek is under water. My bus can't cross. Remember: never walk or play in flood water. It can be deeper and faster than it looks." Card: Can't travel.
- Stop 3, the school: Principal Tran by the gate: "A big tree fell on the gym roof. School is closed today while workers make it safe." Card: No school.
- Stop 4, Mrs. Abbott on her porch: "A tree fell across my driveway, and I can't drive to the store. I'm OK, but I'm stuck at home." Card: Stuck at home.
- The child taps the card that matches. Wrong: "Listen again: what changed for [name]?" and the line replays. Each stop ends with a small smile: everyone is safe.

**Helpers (focus: three rings).** A map of Willow Street in the middle of three rings: On our street (inner), From the next state (middle), From far away (outer). Helper cards come one at a time, each with a picture and a spoken line:
- Neighbors with saws and rakes clearing Mrs. Abbott's driveway (On our street).
- Mr. Diaz's neighbor bringing him a cooler of ice (On our street).
- A power line crew in bucket trucks: "We drove here from the next state to help get the lights back on." (From the next state)
- Town road workers putting up a "Road closed" sign by the creek (On our street).
- A line crew from Canada: "We came from another country! Power crews help each other after big storms." (From far away)
- A Red Cross truck with water and blankets that drove from across the country (From far away).
The child drags each to its ring. Wrong ring: the helper's line replays. When all six are placed: "Lots of people help after a storm, from right next door and from far away."

**I can help (focus: five action cards).** "Kids can help too. Pick one." Five cards:
- Make a card for Mrs. Abbott (result: she puts it on her fridge and smiles).
- Put coins in a jar for the food bank (result: the jar goes to the food bank and becomes food for families).
- Help a grown-up carry water bottles to a neighbor (result: Mr. Diaz has water while the power is out).
- Check on an older neighbor with a grown-up (result: Mrs. Abbott has someone to talk to).
- Pick up small sticks in your own yard with a grown-up (result: the yard is safe to play in).
Each card shows "with a grown-up" where it applies. The child taps one; the result plays. The child can try others.

**Poster (focus: the poster maker).** A blank poster with three parts:
1. Picture: the child's chosen action picture (or draw one).
2. Reason: pick one of three reasons for that action (for "Make a card": "It helps someone feel cared for", "It's fun to draw", "It makes a mess"); the right two are accepted, the silly one bounces: "Does that tell why it helps?"
3. Ending: "You can help too!" plus one picked line ("Ask a grown-up how", "Every little bit helps").
`Read my poster` reads it aloud. `Print` prints it.

## Content
- Four stops, four "what changed" cards, six helpers in three rings (3 on our street, 1 from the next state, 2 from far away), five actions with results, reasons for each action (two good, one silly), two ending lines.
- Willow Street and everyone on it are made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Read my poster` shows only when all three poster parts are filled. `Helpers` opens after the fourth stop; before then its hint names the next stop.
- Keyboard: Tab to a helper card, Enter to pick up, arrow keys to choose a ring, Enter to drop.
- With Motion off trucks appear in their rings without driving, and results appear without animation.

## Look
- Accent `--brand` #2c5f6c after-storm teal (header, rings, card frames); gold #f4c542 (the sun, the active stop, the poster frame); paper #eff6f7; ink #0a2026; muted #4b5c60. The scenes are bright and calm.
- Contrast (WCAG 2.1, computed): white on brand 7.09:1; brand on paper 6.48:1; ink on paper 15.39:1; muted on paper 6.40:1; ink on gold 10.35:1.
- Never color alone: cards and rings carry icons and words.
- Different from this batch (piggy rose, pen pal indigo, carousel red-brown, three towns olive).

## Art
- People art goes to Gemini with `people: true`: Mr. Diaz, Ms. Kaye, Principal Tran and Mrs. Abbott (3 poses each: talking, smiling, waving; cutout yes); helpers: neighbors with rakes, a neighbor with a cooler, a line crew in bucket trucks, town road workers, a Canadian line crew, Red Cross volunteers (6 scenes, 4:3, everyone calm and smiling); result scenes for five actions (5, 4:3).
- Local FLUX (`scripts/localart.py`): Willow Street the morning after (16:9, sunny, branches on lawns, no damage to houses up close); the creek road with a "Road closed" sign (1); the school with a tree on the gym roof seen from far away (1); four action card pictures (5, 1:1).
- Drawn in code: the street map and dots, the rings, cards, the poster frame and parts.
About 29 images.

## Voice
Four bank voices, each unique in this batch: `warm-teacher` as the narrator and Principal Tran; `friendly-dad` as Mr. Diaz; `clear-teacher` as Ms. Kaye; `gentle-storyteller` as Mrs. Abbott. Helper lines use the narrator. `Curio.voice` with `scope: () => state.mode + ':' + state.stop + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Last night a big storm blew through. This morning it's calm and sunny. Let's walk down Willow Street and see how everyone is doing. Tap the first house."
- event, whole, each stop's line.
- how `card` (once): "What changed for them? Tap a card."
- event `card-no`: "Listen again: what changed for [name]?"
- how `helpers`: "Who is helping? Drag each helper to how far they came."
- event, whole, each helper's line; `helpers-done`: "Lots of people help after a storm, from right next door and from far away."
- how `act`: "Kids can help too. Pick one."
- event, whole, each result.
- how `poster`: "Make a poster. Pick a picture, a reason, and an ending."
- event `bounce`: "Does that tell why it helps?"
- event, whole, `poster-read`: the poster read aloud.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the stop walk, card match, the three-ring sort, action results, and the poster maker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Stops | Tap cards in order | The four stops each need a different card; a wrong one replays the line. |
| Rings | Put all helpers on our street | Three of six belong farther out; wrong drops replay the helper's "where we came from" line. |
| Action | Pick any | Any action is right; the result shows what it does. |
| Poster | Pick the silly reason | It bounces with the hint; the poster reads only with a real reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a house: its line (whole), waits; `card` (once); tap: chime or `card-no`.
2. After four stops: `helpers`; each card: its line (whole); drops; `helpers-done` (whole).
3. `act`; a pick: its result (whole).
4. `poster`; parts; `bounce` if needed; `Read my poster`: `poster-read` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.12, D4.6, D4.7 and D4.3 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Big storms can cut power, flood roads, close schools and block driveways with fallen trees | Ready.gov (FEMA), "Hurricanes" and "Power outages" | National Weather Service, storm and flood safety pages | yes |
| Food in a fridge without power for more than about 4 hours may need to be thrown out | FoodSafety.gov, "Food safety during power outages" | USDA Food Safety and Inspection Service, "Keeping food safe during an emergency" | yes |
| Never walk or drive through flood water; it can be deeper and faster than it looks | National Weather Service, "Turn Around Don't Drown" | Ready.gov (FEMA), "Floods" | yes |
| Power line crews travel from other states, and from Canada, to help restore power after big storms (mutual assistance) | Edison Electric Institute, "Mutual assistance" | Hydro-Québec and U.S. utility news on crews sent after Hurricane Sandy (2012) | yes |
| The American Red Cross brings water, blankets and shelter after disasters | American Red Cross, "Disaster relief" | Ready.gov (FEMA), "Volunteer and donate" | yes |
| Children can help after disasters in safe, simple ways with grown-ups (cards, donations, checking on neighbors) | Ready.gov Kids, "Ready Kids" | American Red Cross, "Pillowcase Project" materials | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: children who have lived through storms. The tool shows only the calm morning after, everyone is safe at each stop, no damage is shown up close, and helpers are the focus. Teacher note included. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r4, 2026-11-09): four stops map to four different cards; helpers split 3, 1, 2 across rings; every action marked "with a grown-up" is one a source lists for kids with an adult; each poster reason set has exactly one silly choice; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map, stop and cards fit; at 680x425 the map hides behind `Map`.
2. Each stop takes only its "what changed" card. (D2.Geo.12.K-2)
3. Six helpers land in their rings: street, next state, far away. (D4.6.K-2)
4. Each of five actions plays its result. (D4.7.K-2)
5. The poster needs a picture, a real reason and an ending, and reads aloud. (D4.3.K-2)
6. No scene shows wind, rain, injury or a damaged home up close; the teacher note is present.
7. `Helpers` and `Read my poster` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no driving trucks; no network requests.

## Open questions
- None for Cory.
