# Festival Parade

## One idea
Five floats from real festivals roll down a parade street, each carried by a kid who celebrates it; the class taps the float's clues (a food, a sound, clothes, the season, the weather) and sorts each one as made by people or given by nature, hears the kid tell how their family celebrates, then watches a dotted line on the world map follow the festival from where it began to the city where that kid's family carried it, so first graders learn that a place's culture and its land and weather both shape a celebration, and that people take their festivals with them when they move.

## Not like
- symbol-spotter (K, concept, this batch): national civic symbols and holidays. Here world cultural festivals and how they travel.
- day-in-the-life (3, concept): daily life and where people live. Here one celebration per place and its journey.
- pen-pal-parcels (2, concept): goods that are traded. Here traditions carried by families who moved.
- three-towns (2, concept): sorting homes and jobs into kinds of towns. Here sorting a festival's clues into people-made and nature-given.
- then-and-now-flip (K, concept, this batch): comparing then and now. Here comparing here and there.

## Who and how
- Grade 1, Social Studies (Geography), module "Cultures Around the World". Standards: D2.Geo.6.K-2 (identify cultural and environmental characteristics of specific places), D2.Geo.7.K-2 (explain why and how people, goods and ideas move from place to place).
- Driver: teacher on the projector with the class calling out, or one child alone; every clue, sort choice and kid story is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Five floats; the parade can be paused or replayed. tool.json `modes: ["Parade", "Map", "Passport"]`, `minutes: "15-25"`, `grades_label: "Grade 1"`.
- Nothing is saved; `Print` prints the passport page.
- Change from the idea card: first graders can't guess the name of a festival they have never met, so the guess is now about each clue (made by people, or given by nature?), which is the D2.Geo.6 skill itself.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.6.K-2 (cultural characteristics) | Tap the food, sound and clothes clues and sort them to "Made by people" | the people basket on the float card | 3 |
| D2.Geo.6.K-2 (environmental characteristics) | Tap the season and weather clues and sort them to "From nature" | the nature basket | 3 |
| D2.Geo.7.K-2 (how and why ideas move) | Tap Follow on the map and hear the kid tell how their family carried the festival to a new city | the dotted line from home place to new city | 4 |

## Screens and modes
Header (kit): title "Festival Parade"; `Parade`, `Map`, `Passport`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A city street lined with cheering families and bunting. A drumbeat plays softly (sound on, as the kit sets it). The first float rolls in from the left and stops in the middle. The welcome is queued (`welcomeAfter: true`): "Here comes the parade! Each float is a festival from somewhere in the world. Tap the float to look closer." First hint: "Tap the float to look closer." The first tap zooms the float and cuts the welcome.

**Parade (focus: the stopped float).** At 1366x768 the float fills the center, its kid waves from the top, five clue spots glow on it, and two baskets sit under it: "Made by people" (two hands) and "From nature" (a sun and a leaf). `Next float` sits at the right edge (shown after the float's sort is done). At 680x425 the baskets sit under the float and the crowd folds away.
- Tap a clue spot: it lifts off as a sticker and its line plays ("Dumplings to share.").
- Drag the sticker (or tap it, then a basket). Right: it drops in with a soft chime. Wrong: it floats back and the kid says the clue's why ("People cook dumplings. Do people make them, or does nature?").
- When all five are sorted, the kid tells their story (whole, about 20 seconds), then `Next float` appears.
- Floats roll in and stop one at a time; the parade never moves while a float is open. Tapping a float in the line at the left edge jumps to it.

**Map (focus: a world map drawn in code).** Each float the class has opened shows as its kid's face on the map at the festival's home place. Tap a face, then `Follow`: a dotted line draws to the new city, and the kid tells how their family brought it there. Lines stay drawn.

**Passport.** One page per festival with its five stickers in two columns (people, nature), its home place and the city it traveled to, and a stamp.

**The end.** After the fifth float, all five floats roll together and the class can clap along to an eight-beat drum pattern made for Curio Class (claps light up in time); no traditional song is used.

## Content
Five floats. For each: kid, home place, five clues (three made by people, two from nature), the kid's story, and the travel line.
1. Lunar New Year, carried by Mei (Chinese American, San Francisco). Home: China (also celebrated across East and Southeast Asia). People: dumplings to share; drums and cymbals for the lion dance; red clothes and red envelopes. Nature: the new moon starts it, between January 21 and February 20; late winter, often cold. Story: "We clean the house, eat dumplings with my grandparents, and get red envelopes. The lion dance is so loud!" Travel: China to San Francisco. "Long ago, people from China came to California to work in the gold mines and build the railroad. By the 1860s they shared New Year with the city, and now there's a big parade."
2. Diwali, carried by Anaya (Indian British, Leicester). Home: India; celebrated by Hindus, Sikhs and Jains. People: sweets called ladoos; rangoli patterns made with colored powder; new clothes. Nature: autumn, between mid-October and mid-November; the nights are getting longer, so lamps glow in the dark. Story: "We light little clay lamps called diyas all around the house. Light wins over darkness!" Travel: India to Leicester, England. "My family moved to Leicester. On Belgrave Road, the whole street lights up."
3. Día de los Muertos, carried by Mateo (Mexican American, San Francisco). Home: Mexico, from Indigenous traditions. People: pan de muerto (sweet bread); papel picado (cut-paper banners); skull face paint called calaveras. Nature: orange marigold flowers called cempasúchil; fall, November 1 and 2. Story: "We make an ofrenda with pictures of family who died, and the foods they loved. It's a happy way to remember them." Travel: Mexico to San Francisco's Mission District. "Families brought it from Mexico, and now there are ofrendas and a walk through the neighborhood."
4. Songkran, carried by Ploy (Thai American, Los Angeles). Home: Thailand. People: pouring water over elders' hands for a blessing; folk dances; jasmine garlands. Nature: April 13; one of the hottest times of the year in Thailand, so cool water feels good. Story: "It's Thai New Year! We pour water on my grandma's hands to wish her a good year, and then we have a big water fight!" Travel: Thailand to Thai Town, Los Angeles. "Every April, Hollywood Boulevard closes for food, dances and Songkran."
5. Carnival, carried by Kezia (Trinidadian British, London). Home: Trinidad and Tobago. People: steel pan drums, first made in Trinidad; feathered costumes; calypso songs. Nature: the dry season; warm sunshine before the rains. Story: "My grandma helps sew the costumes. The steel pans go ping-ping-ping all day!" Travel: Trinidad to Notting Hill, London. "People from the Caribbean moved to London. Claudia Jones from Trinidad started a carnival there, and since 1966 it fills the streets every August."
- Sorting keys: food, music, dance, clothes, decorations and customs are made by people; moon, season, weather and flowers are from nature. Every float has exactly three people clues and two nature clues.
- Teacher note: each kid's story is how one family celebrates; families celebrate in many ways, and some children in the class may celebrate these festivals. Día de los Muertos is about remembering family who died, told gently.

## Interactions in detail
- Every tap acts at once; a new line stops the old one. The parade never rolls while a float is open, so nothing moves while a child is sorting.
- `Next float` shows only after the sort is done and the story has started; the hint before then says "Tap a glowing clue." and never names `Next float`.
- `Follow` on the map shows only after a face is tapped.
- With Motion off floats appear in place without rolling and map lines draw all at once.

## Look
- Accent `--brand` #6a1b9a festival purple (header, float frames, baskets); gold #f4c542 (clue glow, passport stamps); paper #f7f0fb; ink #220a30; muted #5e5066. Scene: a city parade street with bunting and a cheering crowd.
- Contrast (WCAG 2.1, computed): white on brand 9.39:1; brand on paper 8.41:1; ink on paper 16.30:1; muted on paper 6.68:1; ink on gold 11.19:1.
- Never color alone: baskets have icons and words; floats' own colors are part of each festival's art, not a cue.
- Different from this batch (forest green, playground blue, brick red, sepia).

## Art
- Local FLUX (`scripts/localart.py`): the parade street and crowd from behind (1, 16:9); five floats, each a painted float with its decorations and an empty spot on top for its kid (5, 16:9); 25 clue stickers in one style (food, instruments, clothes, decorations, moon, flowers, sun, rain clouds) (25, 1:1).
- People art goes to Gemini (`people: true`): Mei, Anaya, Mateo, Ploy and Kezia, each about six, in festival clothes, 4 poses (waving on the float, talking, laughing, clapping); "illustrated six-year-old <name and festival clothes> <pose>, soft gouache, plain white background, big clear face"; 3:4; cutout yes. A fresh agent checks clothes and decorations for accuracy and respect.
About 51 images. Drawn in code: the world map, dotted lines, baskets, passport frames.

## Voice
Bank voice `lively-host` as the narrator (unique in this batch); kids styled as six-year-olds: Mei `upbeat-guide`, Anaya `bright-teacher`, Mateo `easy-coach`, Ploy `curious-librarian`, Kezia `clear-teacher` (each unique in this batch). `Curio.voice` with `scope: () => state.mode + ':' + state.float`, `welcomeAfter: true`.
- how `welcome`: "Here comes the parade! Each float is a festival from somewhere in the world. Tap the float to look closer."
- how `sort` (first float only): "Tap a glowing clue to hear it. Then drag it: made by people, or from nature?"
- event `clue`: each clue line (25).
- event `right`: a soft chime, no words.
- event `why`: the kid's why line for a wrong drop ("People cook dumplings. Do people make them, or does nature?").
- event, whole, `story`: each kid's story.
- how `next`: "Tap Next float to see the next one."
- how `map`: "Tap a kid on the map. Then tap Follow."
- event, whole, `travel`: each kid's travel line.
- event, whole, `finale`: "That's the whole parade! Clap along with the drums."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: float stop-and-open, five clue stickers with two baskets, the travel map with dotted lines, the passport and the clap-along.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put everything in one basket | Each float has three people and two nature clues; wrong drops float back. |
| Sort | Count: the last two go to nature | Clue spots are shuffled on each float, and the basket counts are not shown. |
| Sort | Sort by sticker color | Sticker colors are mixed (orange marigold and orange papel picado go to different baskets). |
| Sort | Guess until it sticks | Allowed; each wrong drop plays the why line first, so the child hears the reason. |
| Map | Tap Follow without watching | The travel line is whole and plays with the line drawing; the passport fills only after it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: drumbeat, `welcome` (queued; may be cut). Tap the float: zoom.
2. First float: `sort` (once). Tap a clue: `clue`. Drop: `right` chime or `why`, each before the next drop counts.
3. Fifth sticker sorted: `story` (whole); then `next` (first time).
4. Map: `map` (first time); Follow: `travel` (whole) while the line draws.
5. After float five: `finale` (whole), then the clap-along.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| D2.Geo.6.K-2 and D2.Geo.7.K-2 wording | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Lunar New Year starts on the new moon between January 21 and February 20; families share dumplings, red envelopes and lion dances | Wikipedia, Chinese New Year (checked 2026-11-09) | Britannica, Lunar New Year | yes |
| Chinese immigrants came to California for the gold mines and railroad, and by the 1860s San Francisco's Chinatown shared New Year with the city | Wikipedia, Chinese New Year (San Francisco section, checked 2026-11-09) | Chinese Historical Society of America, history of the San Francisco parade | yes |
| Diwali is a festival of lights for Hindus, Sikhs and Jains, between mid-October and mid-November, with diya lamps and rangoli | Wikipedia, Diwali (checked 2026-11-09) | Britannica, Diwali | yes |
| Leicester's Diwali celebrations center on Belgrave Road | Wikipedia, Leicester (checked 2026-11-09) | BBC Leicester, "Diwali in Leicester" | yes |
| Día de los Muertos (November 1 and 2) has Indigenous roots, uses ofrendas, marigolds (cempasúchil) and calaveras, and is on UNESCO's list as practiced by the Indigenous communities of Mexico | Wikipedia, Day of the Dead (checked 2026-11-09) | UNESCO, "Indigenous festivity dedicated to the dead" (2008) | yes |
| Día de los Muertos is celebrated in San Francisco's Mission District | Wikipedia, Day of the Dead (California section, checked 2026-11-09) | Smithsonian Latino Center, Día de los Muertos | yes |
| Songkran is Thai New Year on April 13, with water poured over elders' hands for blessings and water fights; on UNESCO's list since 2024 | Wikipedia, Songkran (Thailand) (checked 2026-11-09) | UNESCO, "Songkran in Thailand, traditional Thai New Year festival" | yes |
| April is one of the hottest months in Thailand | Thai Meteorological Department, climate of Thailand (summer mid-February to mid-May) | Britannica, Thailand: climate | yes |
| Thai Town in Los Angeles celebrates Songkran on Hollywood Boulevard in April | Wikipedia, Thai Town, Los Angeles (checked 2026-11-09) | Los Angeles City, Thai Town Songkran festival notice | yes |
| Steel pan drums were first made in Trinidad and Tobago, and Carnival there falls before Lent in the dry season | Britannica, steel band | Wikipedia, Trinidad and Tobago Carnival | yes |
| Notting Hill Carnival has run since 1966 on the August bank holiday weekend; Trinidadian activist Claudia Jones started its forerunner | Wikipedia, Notting Hill Carnival (checked 2026-11-09) | BBC, Black history: Notting Hill Carnival | yes |
Backed twice: 12. Cut: 0.

Sensitivity note: religious and cultural festivals, a festival about family who died, and five kids from five backgrounds. Credits are from each festival's own history (Indigenous roots of Día de los Muertos, Claudia Jones for Notting Hill). A fresh agent reviews clues, stories and art before build.

Checks run (Python, scratchpad r1, 2026-11-09): the saved pages contain "between 21 January and 20 February", "By the 1860s", "mid-October and mid-November", "Belgrave Road", "November 2", "indigenous communities of Mexico", "13 April", "Songkran" on the Thai Town page, "1966" and "Claudia Jones"; each float has three people and two nature clues; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the float and baskets fit; at 680x425 the crowd folds.
2. Every clue, story and choice is spoken; the parade is still while a float is open.
3. Each float's five clues sort into made by people and from nature. (D2.Geo.6.K-2)
4. Each kid's travel line draws on the map with their story. (D2.Geo.7.K-2)
5. The passport shows each festival's two columns and its two places, and prints.
6. Next float and Follow are never named before they show.
7. Tap while it plays: any tap during a line or story acts at once; no older line plays after a newer one.
8. Motion off: floats appear without rolling; no network requests.

## Open questions
- Sensitivity review of the five festivals, kids' stories and art (default used: a fresh agent reviews before build).
- Idea card change: the guess is about each clue (people or nature), not the festival's name (default used: as written here).
