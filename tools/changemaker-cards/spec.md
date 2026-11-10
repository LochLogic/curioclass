# Changemaker Cards

## One idea
A card album holds six real people who made their communities better, but each card starts face down showing only a "before" picture (a crowded city with no green space, a farm family far from any library), and the child flips it piece by piece by asking good questions from a wheel (Who? What was wrong? What did they do? What changed?) while questions that don't help ("What was their favorite food?") flip nothing; the full album then lines up on a timeline from 1858 to 2015, so a second grader learns to ask questions about the people behind a change and sees that people have worked to improve communities for a long time and in many ways.

## Not like
- tools-for-change (5, concept): grade 5 strategies for a local problem. Here asking questions about real changemakers.
- symbol-spotter (K, spec): national symbols and holidays. Here individual people and the change each one made.
- storm-helpers (2, concept, next batch): helpers after one storm. Here many people across time.
- my-life-timeline (1, spec, this batch): ordering one child's life. Here ordering changes across 157 years.
- wonder-kite (1, spec, this batch): small questions that build a big answer. Here questions that reveal one person's story.

## Who and how
- Grade 2, Social Studies (History and Civics), module "Heroes and Changemakers". Standards: D2.His.3.K-2 (generate questions about individuals and groups who have shaped a significant historical change), D2.Civ.14.K-2 (describe how people have tried to improve their communities over time).
- Driver: teacher on the projector with the class choosing questions, or one child alone; every card, question and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Two parts: Flip the cards (six cards), Album timeline. Extra: My changemaker (a blank card). tool.json `modes: ["Cards", "Timeline", "My changemaker"]`, `minutes: "15-30"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.3.K-2 | Spin or tap the wheel to ask Who, What was wrong, What did they do and What changed; skip the questions that don't help | each good question flipping one quarter of the card; a weak question flipping nothing with a reason | 2, 3 |
| D2.Civ.14.K-2 (ways) | Tag each finished card with how the person helped: Building, Speaking up, Helping, Voting, Showing up | the card's way badge | 4 |
| D2.Civ.14.K-2 (over time) | Drag the six cards onto the album timeline from long ago to today | the timeline from 1858 to 2015 with every card in place | 5 |
| D2.His.3.K-2 (own questions) | Ask the four questions about someone you know on a blank card | My changemaker card filled with the child's answers | 6 |

## Screens and modes
Header (kit): title "Changemaker Cards"; `Cards`, `Timeline`, `My changemaker`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** An open card album with six empty slots and one card lying face down on the table, showing a "before" picture: a crowded city street with no trees. A question wheel with four colored parts (each with an icon and words) sits beside it. The welcome is queued (`welcomeAfter: true`): "This card shows a place before someone changed it. Who changed it? Ask a question to find out. Tap Who on the wheel." First hint: "Tap Who on the wheel." The first tap on the wheel asks that question and cuts the welcome.

**Cards (focus: the card in play).** At 1366x768 the card is center and large (split into four quarters), the wheel is at the right, and the album's slots run along the bottom. At 680x425 the album folds into an `Album` button.
- The wheel has four good questions: Who? (a face icon), What was wrong? (a cloud), What did they do? (a hand), What changed? (a sun). Below it, a `More questions` drawer holds weak ones that sound fun but don't help: "What was their favorite food?", "Did they have a dog?", "What color was their hat?"
- A good question flips its quarter and the answer plays (whole). A weak one: "That's fun to wonder, but does it tell us about the change? Try another." Each card needs all four good questions.
- When four quarters are open, the child taps a way badge: Building (a brick), Speaking up (a speech bubble), Helping (two hands), Voting (a ballot box), Showing up (footsteps). Right: the badge stamps. Wrong: "Think about what they did. [What did they do answer]."
- The card goes into its album slot; the next face-down card comes out.
- Six cards (in this order of play, not date order):
  1. Before: a crowded city with no trees. Who: Frederick Law Olmsted, with his partner Calvert Vaux. What was wrong: New York City was crowded and had no big green place for everyone. What they did: In 1858 they won a contest with their plan for Central Park. What changed: A giant park anyone can visit, and many more parks like it. Way: Building.
  2. Before: a farmhouse far down a country road. Who: Mary Lemist Titcomb, a librarian in Maryland. What was wrong: Farm families lived too far away to get to the library. What she did: In 1905 she sent out a book wagon pulled by horses. What changed: The library came to them. Book wagons became bookmobiles, which still visit towns today. Way: Helping.
  3. Before: a line of men voting and a woman turned away. Who: Susan B. Anthony. What was wrong: Women were not allowed to vote. What she did: In 1872 she voted anyway and was arrested. She spoke up for women's votes all her life. What changed: In 1920, after she died, a change to the Constitution let women vote. Way: Voting.
  4. Before: a flooded town with nobody coming to help. Who: Clara Barton, a nurse. What was wrong: When floods, fires and storms hit, there was no group across the country ready to bring help. What she did: In 1881 she started the American Red Cross. What changed: The Red Cross still helps people after disasters. Way: Helping.
  5. Before: two school doors, one marked for Black children and one for white children. Who: Ruby Bridges, age 6. What was wrong: In many places, Black children and white children had to go to different schools. What she did: In 1960 she became the first Black child at William Frantz Elementary School in New Orleans. Some grown-ups were angry, so marshals walked with her to keep her safe. She kept going every day. What changed: Schools began to open to all children. Way: Showing up.
  6. Before: a school bookshelf where every main character looks the same. Who: Marley Dias, age 11. What was wrong: She rarely found books where a Black girl was the main character. What she did: In 2015 she started a book drive called 1000 Black Girl Books. What changed: In a few months people gave more than 9,000 books, and many went to kids who wanted them. Way: Speaking up.
- Two cards are Helping; every other way has one card, so the child must think, not count.

**Timeline (focus: the album timeline).** A long line from "Long ago" (left) to "Today" (right), with year marks at 1850, 1900, 1950 and 2000. The six cards sit in a stack; each shows its year in its "What did they do" quarter. Six spots sit on the line at their true years. The child drags each card to a spot. Right: it snaps with its year; wrong: "Was [year] before or after [nearest placed year]?" When all six are in place: "People have been making their towns better for a long, long time, in lots of ways. And people are still doing it today."

**My changemaker (focus: a blank card).** "Do you know someone who made your school or town better?" The child draws a face with a finger or mouse, then answers the four questions by choosing picture tiles or typing a few words (a teacher, a neighbor, a coach, a family member; fixed a playground, cleaned up a park, started a food drive). The card stays on screen only and prints with `Print`. A line under the card: "Your card stays on this screen. It is never sent anywhere."

## Content
- Six cards: before picture, four answers, way, year. Five ways. Three weak questions. Picture tiles for My changemaker: 8 people, 8 actions, 8 changes.

## Interactions in detail
- Every tap acts at once; a new line stops the old one, except whole answers, which finish before the next answer starts (a tap on another quarter during an answer queues that answer).
- The way badges show only after all four quarters are open. `Timeline` opens after six cards; before then its hint names how many are left.
- Keyboard: Tab to the wheel's parts, Enter to ask; Tab to a timeline card, arrow keys to move, Enter to drop.
- With Motion off quarters change without flipping and cards appear in slots without sliding.

## Look
- Accent `--brand` #5e2d84 album purple (header, card backs, the timeline); gold #f4c542 (the open quarter's edge, way stamps, the placed card's ring); paper #f6f1fa; ink #1c0b29; muted #5d5366.
- Contrast (WCAG 2.1, computed): white on brand 9.61:1; brand on paper 8.64:1; ink on paper 16.72:1; muted on paper 6.52:1; ink on gold 11.43:1.
- Never color alone: wheel parts carry icons and words; ways carry icons and words.
- Different from this batch (timeline terracotta, kite sky blue, council green, backpack mustard).

## Art
- People art goes to Gemini with `people: true`: six respectful illustrated portraits of real people (Olmsted, Titcomb, Anthony, Barton, Ruby Bridges as a six-year-old in 1960, Marley Dias as an eleven-year-old in 2015), each checked against public photos for likeness and dignity (3:4, cutout no); six "after" scenes that include people (Central Park with families, a book wagon at a farmhouse, women voting, Red Cross helpers, a classroom with children of many backgrounds, kids reading) (6, 4:3).
- Local FLUX (`scripts/localart.py`): six "before" scenes without faces in focus (6, 4:3; the voting and school door scenes are drawn calmly, showing a sign and a closed door rather than people being hurt); picture tiles for My changemaker (24, 1:1).
- Drawn in code: card backs, quarters, the wheel, way badges, the album and timeline.
About 42 images.

## Voice
Bank voice `news-reader` as the narrator and card reader (unique in this batch), style: warm storyteller news voice, never dramatic. `Curio.voice` with `scope: () => state.mode + ':' + state.card + ':' + state.q`, `welcomeAfter: true`.
- how `welcome`: "This card shows a place before someone changed it. Who changed it? Ask a question to find out. Tap Who on the wheel."
- event, whole, each answer (24 lines, listed in Cards).
- event `weak`: "That's fun to wonder, but does it tell us about the change? Try another."
- how `way` (once): "How did they help? Tap a way."
- event `way-no`: "Think about what they did." then the card's What did they do answer.
- how `timeline`: "Drag each card to when it happened, from long ago to today."
- event `time-no`: "Was [year] before or after [year]?"
- event, whole, `all-time`: "People have been making their towns better for a long, long time, in lots of ways. And people are still doing it today."
- how `mine`: "Do you know someone who made your school or town better? Draw them, then answer the four questions."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the four-quarter card, question wheel and weak-question drawer, way badges, album slots, the timeline with six year spots, and the blank card's drawing canvas.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Questions | Tap the wheel in order without listening | Allowed for flipping, but the way badge and timeline need the answers; a wrong way replays the key answer. |
| Questions | Use the weak ones | They flip nothing and say why. |
| Ways | Tap Helping every time | Only two of six are Helping. |
| Timeline | Place by guessing | Each wrong drop names a placed year to compare; years show on the cards and the spots, so reading and comparing them is the skill. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a wheel part: its answer (whole).
2. Each good question: answer (whole); weak: `weak`.
3. Four quarters: `way` (once); tap: stamp or `way-no`.
4. Six cards: `timeline`; drops: snap or `time-no`; all placed: `all-time` (whole).
5. My changemaker: `mine`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.3.K-2 and D2.Civ.14.K-2 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Olmsted and Vaux's Greensward Plan won the Central Park design contest in 1858 | Wikipedia, Frederick Law Olmsted (checked 2026-11-09) | Central Park Conservancy, "Park history" | yes |
| Mary Lemist Titcomb, librarian of the Washington County Free Library in Hagerstown, Maryland, started a book wagon in 1905, an early bookmobile | Wikipedia, Bookmobile and Mary Lemist Titcomb (checked 2026-11-09) | Maryland State Archives, Women's Hall of Fame, Mary Lemist Titcomb | yes |
| Susan B. Anthony voted in 1872 and was arrested; the 19th Amendment (1920) gave women the right to vote; she died in 1906 | Wikipedia, Susan B. Anthony (checked 2026-11-09) | National Park Service, Susan B. Anthony and the 19th Amendment | yes |
| Clara Barton founded the American Red Cross on May 21, 1881 | Wikipedia, Clara Barton (checked 2026-11-09) | American Red Cross, "Founder Clara Barton" | yes |
| Ruby Bridges, age 6, desegregated William Frantz Elementary School in New Orleans on November 14, 1960, escorted by federal marshals | Wikipedia, Ruby Bridges (checked 2026-11-09) | National Women's History Museum, Ruby Bridges biography | yes |
| Marley Dias started #1000BlackGirlBooks in November 2015 at age 11; more than 9,000 books were collected within a few months | Wikipedia, Marley Dias (checked 2026-11-09) | Scholastic, Marley Dias and 1000 Black Girl Books | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: real people's stories, including segregation (Ruby Bridges) and race in children's books (Marley Dias). Tellings are short, factual and calm; the before scenes show signs and closed doors, not people being hurt or shouted at. Marley Dias is a living public figure; her card uses only her public campaign. A fresh-agent sensitivity read is needed before build, and Cory may want to choose the six.

Checks run (Python, scratchpad r3, 2026-11-09): years 1858, 1872, 1881, 1905, 1960, 2015 are in order and each has its own spot at its true year, so order is exact; Anthony's 1906 death is before 1920; Ruby Bridges's age 6 and Marley Dias's age 11 match the sources; ways count 2 Helping and 1 each of the other four; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 card, wheel and album fit; at 680x425 the album folds.
2. Each of the four good questions opens one quarter of each card. (D2.His.3.K-2)
3. Weak questions open nothing and say why. (D2.His.3.K-2)
4. Each card takes only its way badge. (D2.Civ.14.K-2)
5. All six cards end on the timeline in year order. (D2.Civ.14.K-2)
6. My changemaker takes a drawing and four answers and stays on screen only. (D2.His.3.K-2)
7. The way badges and `Timeline` are never named before they show.
8. Tap while it plays: a tap during an answer queues the next answer; no older line plays after a newer one.
9. Motion off: no flips or slides; no network requests.

## Open questions
- Are these the right six people for a grade 2 album (default used: Olmsted, Titcomb, Anthony, Barton, Ruby Bridges, Marley Dias; a mix of times, ways, women and men, famous and less known)?
- Ruby Bridges's way: "Showing up" was added as a fifth way because she was a child who kept going, not a speaker or builder (default used: Showing up).
