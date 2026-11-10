# The Last Carousel Ride

## One idea
The old carousel in Linden Park stopped for good in 1975, and two honest people remember why differently (Ms. Dottie, who rode it as a girl, remembers the big white horse breaking and never being fixed; Ben, the owner's grandson, remembers his grandpa saying too few people came and the motor cost too much to fix), so the child lays their two tellings side by side to see what they agree on and what differs, gathers three more clues (a 1975 newspaper clipping, a ticket price board, the owner's rider count book), pins clues to possible reasons on a reason board, and picks the most likely reason (or two working together) by how many clues hold it up, then hears the full story and why two people remembered one day two ways.

## Not like
- capsule-from-1965 (1, spec): reading objects for maker, date and place. Here two accounts of one event and its causes.
- why-the-pony-express-ended (5, concept): a grade 5 evidence claim. Here the first steps of comparing accounts and weighing reasons.
- changemaker-cards (2, spec): real people who made change. Here a made-up town's small mystery.
- my-life-timeline (1, spec): one life in order. Here one day's causes.

## Who and how
- Grade 2, Social Studies (History), module "The Last Carousel Ride". Standards: D2.His.6.K-2 (compare different accounts of the same historical event), D2.His.14.K-2 (generate possible reasons for an event or development in the past), D2.His.16.K-2 (select which reasons might be more likely than others to explain a historical event or development).
- Driver: teacher on the projector with the class, or one child alone; every telling, clue and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Four parts: Two tellings, Clues, Reason board, What really happened. Extra: class vote. tool.json `modes: ["Mystery", "Class vote"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.
- The page says, under the title: "Linden Park and its carousel are made up for this mystery."

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.6.K-2 | Drag parts of the two tellings into "Both say" or "Only one says" | the side-by-side tellings and the two sorted columns | 2 |
| D2.His.14.K-2 | Put possible reasons on the reason board, including your own from the reason cards | the board with up to six reason cards | 3 |
| D2.His.16.K-2 | Pin each clue to the reasons it supports, then pick the most likely reason by clue count | pins on each reason and the child's pick | 4, 5 |
| D2.His.6.K-2 (why they differ) | Hear why each person remembered it their way and match the person to what they saw | the two people and "what they saw" cards | 6 |

## Screens and modes
Header (kit): title "The Last Carousel Ride"; `Mystery`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** Linden Park on a fall day: a carousel under a big tarp, a faded "Closed" sign, a bench beside it. The welcome is queued (`welcomeAfter: true`): "This carousel stopped running in 1975, and it never ran again. Why did it stop? Tap the bench to meet someone who remembers." First hint: "Tap the bench to meet someone who remembers." The first tap brings Ms. Dottie to the bench and cuts the welcome.

**Two tellings (focus: the bench, then the two columns).** 
- Ms. Dottie (now about 60; she was 10 in 1975): "I rode that carousel every Saturday. My favorite was the big white horse. One summer it broke, its leg cracked, and they never fixed it. On the last day, everybody was sad. I think it closed because it broke."
- Then `Meet Ben` brings Ben (about 40), whose grandpa, Walt Kerr, owned it: "My grandpa told me the story. He said fewer and fewer people came to ride. Then the old motor needed fixing, and it cost too much. He was sad to close it."
- At 1366x768 the two tellings sit side by side as speech cards broken into short parts; under them are two columns, "Both say" (an equal sign) and "Only one says" (two different shapes). At 680x425 one telling shows at a time with a toggle.
- The child drags each part:
  - Both say: "It closed in 1975." / "The last day was sad." / "Something was broken."
  - Only one says: "The white horse broke." (Dottie) / "Fewer people came." (Ben) / "The motor cost too much to fix." (Ben)
  - Wrong drop: "Did both of them say that? Listen again." and the two matching parts play.

**Clues (focus: a table of three clues).** Three clue cards, each opened by tap, read aloud with its key part lit:
1. Newspaper clipping, Linden Gazette, August 1975: "Carousel to close September 1. Owner Walt Kerr says riders have dropped by half since the new Northgate Mall opened in 1972. Fixing the carousel's motor would cost 8,000 dollars."
2. Ticket price board: "1965: 10 cents. 1975: 25 cents."
3. Mr. Kerr's rider book: "1970: 40,000 riders. 1974: 18,000 riders." Shown as two stacks of ticket pictures, the 1974 stack less than half as tall.
Each clue opens a "What does it tell us?" line after reading.

**Reason board (focus: the board).** Six reason cards, each a picture plus words: "Parts broke", "Fewer people came", "A new mall opened", "The owner got old", "Rides cost more", "Bad weather". The child drags any reasons they think could be true onto the board (at least three). Then the child drags clue pins (one pin per source: Dottie, Ben, Newspaper, Price board, Rider book) onto every reason that source supports. A pin on a reason it doesn't support bounces: "Does [source] say anything about that?"
- Supports (checked in Python): Parts broke: Dottie, Ben, Newspaper (3). Fewer people came: Ben, Newspaper, Rider book (3). A new mall opened: Newspaper (1). Rides cost more: Price board (1). The owner got old: none. Bad weather: none.
- Then: "Which reason is most likely? Tap one, or tap two that work together." With `Two together` the child can pick two.
- Picks and replies:
  - Parts broke, or Fewer people came, alone: "That has three clues! But look: both have three. Could they work together?"
  - Both together: gold stars: "Yes! Two reasons with the most clues."
  - A one-clue reason: "That has one clue. Is there a reason with more?"
  - A no-clue reason: "No clue says that. What do the clues say?"

**What really happened (focus: a picture story).** Four pictures, read aloud: fewer people came after the mall opened in 1972 (with its own rides inside); with fewer riders, there was less money; in 1975 the motor and the white horse needed fixing and it cost too much; so Mr. Kerr closed it. Then: "Ms. Dottie was a kid. She saw her favorite horse break. Ben heard his grandpa talk about money. They both told the truth. They each saw a different part." A matching step: drag "saw the broken horse" to Dottie and "heard about money" to Ben.
- `Print` prints the two columns, the board with pins, and the child's pick.

**Class vote.** The reason board with tally buttons for each reason, then the clue count reveal.

## Content
- Two tellings in six parts; three clues; six reasons; five sources as pins; a four-picture ending; two "what they saw" cards. All made up for the tool.

## Interactions in detail
- Every tap acts at once; a new line stops the old one, except whole tellings.
- `Meet Ben` shows after Dottie's telling ends. `Two together` shows after the pins are placed. Clues open after the columns are done; the hint names the next step.
- Keyboard: Tab to a part or pin, Enter to pick up, Tab to a column or reason, Enter to drop.
- With Motion off pins drop without bouncing and the tarp doesn't flap.

## Look
- Accent `--brand` #8b2e2e old carousel red (header, the board frame, ticket stubs); gold #f4c542 (pins, stars, the lit clue line); paper #fbf2ef; ink #2a0c0c; muted #68514e.
- Contrast (WCAG 2.1, computed): white on brand 8.31:1; brand on paper 7.54:1; ink on paper 16.47:1; muted on paper 6.62:1; ink on gold 11.17:1.
- Never color alone: columns carry symbols and words; pins carry source icons and names.
- Different from this batch (piggy rose, pen pal indigo, storm teal, three towns olive).

## Art
- People art goes to Gemini with `people: true`: Ms. Dottie now (4 poses) and as a 10-year-old on the white horse (1, inside a memory frame); Ben (4 poses); Walt Kerr in 1975 (2 pictures, in Ben's memory frame); the ending's four pictures (4, 4:3).
- Local FLUX (`scripts/localart.py`): Linden Park with the tarp (16:9); the carousel running in its day (1, 4:3, in a memory frame); the white horse with a cracked leg (1); six reason pictures (6, 1:1).
- Drawn in code: the newspaper clipping (text in a period type), the price board, the rider book's ticket stacks, columns, the board and pins.
About 26 images.

## Voice
Three bank voices, each unique in this batch: `knowing-guide` as the narrator and clue reader; `wise-mentor` as Ms. Dottie; `hero-coach` as Ben. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "This carousel stopped running in 1975, and it never ran again. Why did it stop? Tap the bench to meet someone who remembers."
- event, whole, `dottie`, `ben`: the tellings.
- how `columns`: "Drag each part to Both say or Only one says."
- event `col-no`: "Did both of them say that? Listen again."
- how `clues`: "Tap a clue to read it."
- event, whole, each clue and its "What does it tell us?" line.
- how `board`: "Drag reasons that could be true onto the board. Then pin each clue to the reasons it supports."
- event `pin-no`: "Does [source] say anything about that?"
- how `pick`: "Which reason is most likely? Tap one, or tap Two together."
- event, whole, the four pick replies.
- event, whole, `story`: the four ending pictures; `both-true`: the "They both told the truth" line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the two-telling columns, clue cards, the reason board with multi-pin support, the pick with "two together", and the ending.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Columns | Drag at random | Six parts; wrong drops replay the matching parts from both tellings. |
| Pins | Pin every source on every reason | Wrong pins bounce with the source named; only true supports stay. |
| Pick | Pick the reason with the most pins without reading | That works only if the pins are right, and the pins needed the reading; a single pick of a three-clue reason asks to look again at the tie. |
| Why they differ | Guess | Two cards, two people; a wrong match replays each person's line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap bench: `dottie` (whole), waits; `Meet Ben`: `ben` (whole), waits.
2. `columns`; drops: chime or `col-no`.
3. `clues`; each tap: clue (whole).
4. `board`; drops and pins; `pin-no` as needed; `pick`; a pick reply (whole).
5. `story` (whole), waits; `both-true` (whole); matching.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.6, D2.His.14 and D2.His.16 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Many old park carousels in the U.S. closed or were sold off in the 1960s and 1970s as fewer people came and repairs grew costly | National Carousel Association, "History of the carousel in America" | Wikipedia, Carousel (checked 2026-11-09), "Golden age" and decline | yes |
| Shopping malls spread across U.S. towns in the 1960s and 1970s | Wikipedia, Shopping mall (checked 2026-11-09), history in the United States | Smithsonian Magazine, history of the American mall | yes |
| Two honest witnesses can remember the same event differently because they saw or heard different parts | Library of Congress, "Analyzing oral histories" (teacher guide) | Oral History Association, "Principles and best practices" | yes |
Backed twice: 4. Cut: 0.

The town, people, newspaper and numbers are made up; they are shaped to match the real pattern in the sources.

Checks run (Python, scratchpad r4, 2026-11-09): pin supports give counts Parts broke 3, Fewer people came 3, New mall 1, Rides cost more 1, Owner got old 0, Bad weather 0, so the top two tie and "two together" is the best pick; 18,000 is less than half of 40,000, matching "dropped by half"; 1972 is before 1975; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both tellings and the columns fit; at 680x425 one telling shows with a toggle.
2. Six parts sort into Both say and Only one says. (D2.His.6.K-2)
3. At least three reasons go on the board. (D2.His.14.K-2)
4. Pins stay only on reasons their source supports. (D2.His.16.K-2)
5. The pick replies match the clue counts, and the two top reasons together earn the stars. (D2.His.16.K-2)
6. The ending explains why Dottie and Ben remember it differently, and the matching step checks it. (D2.His.6.K-2)
7. `Meet Ben` and `Two together` are never named before they show.
8. Tap while it plays: a tap during a line acts at once except whole tellings; no older line plays after a newer one.
9. Motion off: no bouncing pins; no network requests.

## Open questions
- None for Cory.
