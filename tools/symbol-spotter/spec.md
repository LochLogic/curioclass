# Symbol Spotter

## One idea
National symbols hide on everyday things on one kitchen table and porch (a flag by the door, a dollar bill, a stamp, a postcard), and each one the child finds opens a one-minute picture story that ends on the idea it stands for (freedom, every state counting the same, welcome, many joined as one), then holiday doors let the child spin a question wheel to ask their own question about the people a holiday honors and hear it answered, so they learn what our symbols mean and how to ask about the people behind our holidays.

## Not like
- festival-parade (1, concept, this batch): world cultural festivals and how they travel. Here national civic symbols and holidays.
- changemaker-cards (2, concept): collecting community changemakers on cards. Here four national symbols and four holidays, and the child's own questions.
- capsule-from-1965 (1, concept): finding who made sources and when. Here what a symbol stands for.
- playground-rules (K, concept, this batch): making rules for a group. Here the ideas a country chose to show on its things.
- me-on-the-map (K, built): where I am. Here what our country's pictures mean.

## Who and how
- Kindergarten, Social Studies (Civics), module "Symbols and Holidays". Standards: D2.Civ.8.K-2 (democratic principles such as equality, fairness and respect for rules), D2.His.3.K-2 (generate questions about people who shaped a significant historical change).
- Driver: teacher on the projector with the class calling out, or one child alone; every story, door and question is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Four symbols, four holiday doors. tool.json `modes: ["Find", "Holiday doors", "Sticker book"]`, `minutes: "10-20"`, `grades_label: "Grade K"`.
- Nothing is saved; `Print` prints the sticker book page.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.8.K-2 (equality) | Find the flag; hear that each of the 50 stars is one state and every state counts the same | the flag story ending on "the same" | 3 |
| D2.Civ.8.K-2 (freedom, fairness) | Find the Liberty Bell stamp; hear its words and how people used it to ask for freedom for all | the bell story ending on "freedom" | 3 |
| D2.Civ.8.K-2 (welcome, unity) | Find the Statue of Liberty postcard and the eagle on the dollar | their stories ending on "welcome" and "out of many, one" | 3 |
| D2.His.3.K-2 | Open a holiday door and build a question with the wheel (Who? Why? What changed?) about the people it honors; hear the answer | the wheel, the question and the answer picture | 4, 5 |

## Screens and modes
Header (kit): title "Symbol Spotter"; `Find`, `Holiday doors`, `Sticker book`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A sunny front porch and an open kitchen window: a flag hangs by the door, and on the kitchen table sit a wallet with a dollar bill sticking out, a letter with a stamp, and a postcard leaning on a cup. Four sparkle spots are hidden among other everyday things (a cat, a lunch box, a plant, keys). The welcome is queued (`welcomeAfter: true`): "Our country has special pictures called symbols. They hide on everyday things. Find something red, white and blue, and tap it." First hint: "Find something red, white and blue, and tap it." The first tap cuts the welcome.

**Find (focus: the porch and table scene).** At 1366x768 the scene fills the screen with the sticker book strip (four empty outlines) along the bottom. At 680x425 the strip folds into a `Sticker book` button.
- Tap an everyday thing that isn't a symbol: its name plays and a little "not a symbol" wiggle ("That's a lunch box. Keep looking!").
- Tap a symbol: it zooms up and its story plays as three painted pictures with one short line each (about 20 seconds in all), then the idea word appears with its picture and the sticker flies to the book. After the first symbol, the hint names the next clue: "Find a bird.", "Find a bell.", "Find a lady holding a torch."
- The four stories:
  - Flag by the door: "This is our flag. It has 50 stars, one for each state. Big states and small states each get one star. Every state counts the same." Idea: the same (equal).
  - Stamp with the Liberty Bell: "This bell is in Philadelphia. Its words say: Proclaim liberty throughout all the land. Long ago, people who wanted slavery to end named it the Liberty Bell. It reminds us of freedom for everyone." Idea: freedom.
  - Postcard of the Statue of Liberty: "This statue stands by the sea in New York. People from France gave it as a gift. For many years, families coming by ship saw her first. She says welcome." Idea: welcome.
  - Dollar bill with the eagle: "On the back of the dollar is our bald eagle. It's the national bird. Its ribbon says, Out of many, one. Many states and many people make one country." Idea: out of many, one.

**Holiday doors (focus: four painted doors on a street).** Each door has a picture and is read on tap: Independence Day (fireworks over a park), Presidents' Day (a portrait frame of George Washington), Martin Luther King Jr. Day (people walking together), Veterans Day (a parade with flags). Tap a door: it opens to one picture and one line about the people it honors. Then the question wheel shows three big wedges with pictures: Who? (a face), Why? (a thought bubble), What changed? (a before-and-after arrow). The child taps a wedge, and the question is built and spoken ("Why did Dr. King march?"), then answered with a picture and two or three short sentences. The child can ask all three; the one they tap "Keep" on goes in the sticker book under that holiday.

**Sticker book.** Four symbol stickers with their idea words, and the child's kept question for each holiday they opened.

**Teacher add.** Teacher notes say how to add a state or local symbol to the scene later; the tool itself ships the four.

## Content
- Symbols and stories as above.
- Holiday doors (people line, then three questions with answers):
  - Independence Day (July 4): "On July 4, 1776, leaders signed the Declaration of Independence." Who? "Leaders from the 13 colonies, like Thomas Jefferson, who wrote most of it." Why? "They wanted to make their own rules, not have a faraway king make them." What changed? "The colonies said they were a new country, the United States."
  - Presidents' Day (third Monday in February): "This day began as George Washington's birthday." Who? "George Washington, the first president." Why? "People wanted to remember the first leader of the new country." What changed? "The country had a president chosen by the people, not a king."
  - Martin Luther King Jr. Day (third Monday in January): "This day honors Dr. Martin Luther King Jr." Who? "Dr. King was a minister who spoke up for fair laws, with many other people." Why? "Some laws kept Black people and white people apart, and that wasn't fair. Dr. King and many others marched peacefully to change those laws." What changed? "Those unfair laws were changed, and people kept working so everyone is treated the same."
  - Veterans Day (November 11): "This day thanks people who served in our military." Who? "Veterans: women and men who served in the Army, Navy, Air Force, Marines, Coast Guard and Space Force." Why? "They worked to keep the country safe." What changed? "People made a day to say thank you, every November 11."
- Teacher note: the King story is kept to what kindergartners can hold; the teacher guide links to grade-level reading on the Civil Rights Movement and suggests how to answer if a child asks about his death (simple, truthful, follow the family's lead).

## Interactions in detail
- Every tap acts at once; a new line stops the old one; tapping another symbol during a story stops it and starts the new one.
- A symbol found twice replays its story; the sticker doesn't double.
- The wheel builds only from its three wedges, so every question makes sense; there is no typing.
- With Motion off stories show their three pictures as a row and stickers appear in the book without flying.

## Look
- Accent `--brand` #8a2432 brick red (header, door frames, the wheel rim); gold #f4c542 (sparkle spots, the kept question star); paper #fbf1f1; ink #2a0b0f; muted #6a5254. Scene: a front porch and a sunny kitchen table.
- Contrast (WCAG 2.1, computed): white on brand 8.83:1; brand on paper 7.97:1; ink on paper 16.44:1; muted on paper 6.43:1; ink on gold 11.20:1.
- Never color alone: wedges and doors have pictures and words; found symbols get a check and a sticker.
- Different from this batch (forest green, playground blue, sepia, festival purple).

## Art
- Local FLUX (`scripts/localart.py`): porch and kitchen table scene with the everyday things as separate cutouts (1 scene, 16:9; 8 cutouts, 1:1); the flag on a porch, the Liberty Bell in its hall, the Statue of Liberty from a ship, a bald eagle in flight (story pictures, 12, 4:3); four holiday door scenes (fireworks over a park, a parade with flags, a portrait frame, a crowd walking together seen from behind at a distance) (4, 3:4).
- People art goes to Gemini (`people: true`): George Washington (portrait style, respectful), Thomas Jefferson writing, Dr. Martin Luther King Jr. speaking to a crowd and walking with marchers, a group of veterans of different ages, genders and races; story and answer pictures, 12 in all; "respectful illustrated portrait <subject>, soft gouache, warm light"; 4:3; cutout no.
- Stamp, bill and postcard frames are painted blank, with any words in code.
About 37 images. Drawn in code: the wheel, sticker book, idea word cards.

## Voice
Bank voice `knowing-guide` as the narrator (unique in this batch), style: friendly museum guide for small children. `Curio.voice` with `scope: () => state.mode + ':' + state.open`, `welcomeAfter: true`.
- how `welcome`: "Our country has special pictures called symbols. They hide on everyday things. Find something red, white and blue, and tap it."
- event `thing`: an everyday thing's name plus "Keep looking!".
- event, whole, `story`: each symbol's three lines (texts in Screens and modes).
- event `idea`: the idea word ("Freedom.").
- how `next-clue`: "Find a bird." / "Find a bell." / "Find a lady holding a torch." / "Find something red, white and blue." (whichever is still hidden; spoken once each, then hint only).
- event, whole, `all-found`: "You found all four symbols! Tap Holiday doors to meet the people our holidays honor."
- how `doors`: "Tap a door to open it."
- event `door`: the door's people line.
- how `wheel`: "Tap a wheel picture to ask a question: Who, Why, or What changed."
- event `question`: the built question.
- event, whole, `answer`: the answer.
- event `kept`: "That question is in your sticker book."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: the find scene with symbols and decoys, the three-picture stories, the doors and the three-wedge question wheel, the sticker book.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Find | Tap everything | Allowed; it's an explorer. Decoys say their names, and only symbols open stories, so tapping everywhere still hears every story. |
| Wheel | Tap wedges at random | Every wedge gives a real question and answer; there's no score. The sticker book keeps the question the child chose. |
This tool has no score or win state, by design (an explorer about symbols and holidays).

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut).
2. Tap a decoy: `thing`. Tap a symbol: `story` (whole, three lines), then `idea`, then `next-clue` (first time each).
3. Fourth symbol: `all-found` (whole) after its story and idea.
4. Doors: `doors` (first time); tap a door: `door`; then `wheel` (first time); tap a wedge: `question` then `answer` (whole); Keep: `kept`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| D2.Civ.8.K-2 and D2.His.3.K-2 wording | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The flag has 50 stars, one for each state, and 13 stripes for the original colonies | Wikipedia, Flag of the United States (checked 2026-11-09) | U.S. Code, Title 4, Section 1 and 2 (the flag) | yes |
| The Liberty Bell's inscription reads "Proclaim LIBERTY Throughout all the Land unto all the Inhabitants Thereof"; abolitionists gave it the name and used it as a symbol of freedom | Wikipedia, Liberty Bell (checked 2026-11-09) | National Park Service, Independence National Historical Park, Liberty Bell | yes |
| The Statue of Liberty was a gift from the people of France, dedicated October 28, 1886, and became a symbol of welcome to immigrants arriving by sea | Wikipedia, Statue of Liberty (checked 2026-11-09) | National Park Service, Statue of Liberty National Monument | yes |
| The bald eagle is on the Great Seal (adopted 1782), which is on the back of the one-dollar bill, with the motto E pluribus unum, "out of many, one"; it is the national bird | Wikipedia, Great Seal of the United States and Bald eagle (checked 2026-11-09) | U.S. Department of State, The Great Seal of the United States | yes |
| Independence Day marks July 4, 1776; Presidents' Day (Washington's Birthday) is the third Monday in February; MLK Day is the third Monday in January, first observed 1986; Veterans Day is November 11 | Wikipedia pages for each holiday (checked 2026-11-09) | 5 U.S.C. 6103 (federal holidays), U.S. Office of Personnel Management holiday list | yes |
| Dr. King led peaceful marches against laws that segregated Black and white Americans, with many others | The King Center, About Dr. King | National Park Service, Martin Luther King Jr. National Historical Park | yes |
| The U.S. Armed Forces are the Army, Navy, Air Force, Marine Corps, Coast Guard and Space Force | U.S. Department of Defense, Our Forces | U.S. Department of Veterans Affairs, Veterans Day | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: national symbols, Dr. King and segregation for kindergarten; the Liberty Bell story credits abolitionists. A fresh agent reviews the holiday stories and portraits before build.

Checks run (Python, scratchpad r1, 2026-11-09): the saved pages contain "50 stars", "LIBERTY Throughout all the Land", "October 28, 1886", "adopted as a national emblem in 1782", "one-dollar bill", "Out of many, one", "third Monday of January", "third Monday of February" and "November 11"; each door has exactly three questions and each wedge builds one; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the scene fills with the sticker strip; at 680x425 the strip folds into a button.
2. Decoys say their names; symbols open their three-picture stories.
3. Each symbol story ends on its idea word and adds a sticker. (D2.Civ.8.K-2)
4. Each holiday door opens with its people line. (D2.His.3.K-2)
5. The wheel builds and speaks a question and its answer; Keep adds it to the book. (D2.His.3.K-2)
6. The sticker book prints.
7. Every hint names a control that is showing.
8. Tap while it plays: any tap during a story acts at once; no older line plays after a newer one.
9. Motion off: stories as rows of pictures; no network requests.

## Open questions
- Sensitivity review of the holiday stories (Dr. King and segregation for kindergarten) and portraits (default used: a fresh agent reviews before build).
