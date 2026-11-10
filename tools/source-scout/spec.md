# Source Scout

## One idea
Before anyone answers "Should recess be longer?", the child scouts a shelf of eight sources (a doctor's article, a parent survey, a toy company ad, the principal's letter, a teacher's blog, a kid's poster, a study on recess and focus, the nurse's playground injury log), flips each one to see who made it, when and why, packs the four that best cover the question and the people who would disagree, then sorts each kept source's sentences into Fact or Opinion and watches its trust meter settle, so a fifth grader learns that good research picks sources by origin and purpose, covers more than one side, and that a true fact chosen to sell something still needs a second source.

## Not like
- made-for-whom (4, spec): infers the audience and purpose of 1870s railroad sources. Here choosing sources for a question and rating their trust.
- why-the-pony-express-ended (5, spec): builds a claim from evidence. Here deciding which sources are worth using before any claim.
- history-article-review (5, spec): critiques a finished article. Here scouting raw sources.
- how-do-you-know (3, spec): primary or secondary. Here fact or opinion and who made it why.

## Who and how
- Grade 5, Social Studies (Inquiry), module "Source Scout". Standards: D1.5.3-5 (determine the kinds of sources that will be helpful in answering compelling and supporting questions, taking into consideration the different opinions people have about how to answer the questions), D3.1.3-5 (gather relevant information from multiple sources while using the origin, structure, and context to guide the selection), D3.2.3-5 (use distinctions among fact and opinion to determine the credibility of multiple sources).
- Format: sort. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every source. Controls 44 px or more.
- Three steps: Scout (flip and pack), Sort (Fact or Opinion), Trust (the meters and a reason line). Extra: a second question, "Should our school have a garden?", with its own shelf. tool.json `modes: ["Recess", "Garden"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D1.5.3-5 | Pack four sources and watch the "Who might disagree?" strip light for each viewpoint covered | the strip (kids, teachers, parents, the principal); a nudge if the pack covers only one side | 2 |
| D3.1.3-5 | Flip each source's tag (made by, when, why, kind) before packing | the tag on the back of each card; packing a source without flipping plays "Flip it first. Who made it?" | 3 |
| D3.2.3-5 | Drag each kept sentence into Fact or Opinion; then write a reason line for each trust meter | the sort trays; trust meters that combine the sort with the maker and purpose | 4, 5 |

## Screens and modes
Header (kit): title "Source Scout"; `Recess`, `Garden`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A scout's clipboard with the question "Should recess be longer?", an empty backpack with four pockets and a shelf of eight source cards. Below, the strip "Who might disagree?" with four unlit figures (kids, teachers, parents, the principal). The welcome is queued (`welcomeAfter: true`): "Before anyone answers this question, a good scout picks good sources. Flip a source to see who made it and why." First hint: "Tap a source to flip it."

**Scout (focus: the shelf and the backpack).** At 1366x768 the shelf runs across the top and the backpack and strip sit below; at 680x425 the shelf scrolls sideways in one row and the backpack pins to the bottom.
- Each card front shows its title and a picture; the back (flipped) shows four tags: Made by, When, Why it was made (to inform, to persuade, to sell, to record), Kind (article, survey, ad, letter, blog, poster, study, log).
- The eight sources (all made for this game, built on real findings):
  1. A children's doctor's article: recess helps kids pay attention and get along (made by a pediatrician, to inform).
  2. A parent survey at Maple School: 41 of 60 parents want longer recess; 12 want more class time; 7 not sure (to record).
  3. Zoom Toys ad: "Kids who play outside move more! Buy the Zoom Ball for every recess!" (to sell).
  4. Principal Ruiz's letter: the school day has a fixed number of minutes and state tests to prepare for (to inform and persuade).
  5. Mr. Bell's teacher blog: "After recess my class settles faster. After a rainy-day recess inside, they don't." (to inform, opinion and observation).
  6. Jayden's poster: "RECESS RULES! Longer recess = happier kids!" (to persuade).
  7. A study summary: classes that got a daily recess had better behavior reports than classes with little or none (to inform).
  8. The school nurse's injury log: playground bumps by month, most on the big slide (to record).
- Packing: drag or tap-then-place into a pocket (four pockets). The strip lights each viewpoint the pack covers: the survey lights parents; the principal's letter lights the principal; the blog lights teachers; the poster lights kids. The doctor's article, the study and the injury log light "facts any side can use". The ad lights nothing.
- When four are packed: `Check my pack`. If all four lean one way: "Your pack only has one side. Who might disagree? Swap one source." A pack with two sides and at least one fact source: "Strong pack. Now let's sort what each source says."

**Sort (focus: one kept source at a time).** Each kept source opens with three to five sentences. The child drags each into Fact (can be checked) or Opinion (what someone thinks or feels). Example sentences: survey "41 of 60 parents who answered want longer recess." (Fact); poster "Longer recess = happier kids!" (Opinion); blog "After recess my class settles faster." (Fact, an observation he could check); principal "Every minute of class time matters." (Opinion). A wrong drop plays a whole-line hint: "Could someone check this, or is it what someone thinks?"

**Trust (the meters).** Each kept source gets a meter from 1 to 5 that settles from three things: how many facts it has, who made it (do they know the subject?), and why it was made (to sell lowers trust). The child picks a reason tile ("made by an expert", "made to sell", "only one person's view", "has numbers I could check", "one side only") and the meter shows the child's reason beside it.
- The ad aha: if the child packed the ad, its one true sentence ("Kids who play outside move more") sorts as Fact, yet its meter stays low. The narrator: "That fact is true. But Zoom Toys picked it to sell balls. Check it in a second source before you use it." A link shows the doctor's article saying the same thing.
- If the child didn't pack the ad, `Peek at the one you skipped` shows it as an example.

**The end.** The clipboard with the four packed sources, their meters and reasons, and the lit strip. Narrator: "A scout doesn't answer the question yet. A scout makes sure the answer will rest on good sources from more than one side." `Print` prints the clipboard.

**Garden (extra).** "Should our school have a garden?" with eight new sources: a farmer's letter, a cafeteria cost sheet, a seed company ad, a teacher survey, a kid's drawing, a study on school gardens and eating vegetables, a custodian's list of summer jobs, and the city's water bill.

## Content
- Two questions, eight sources each, three to five sentences per kept source with answers (Fact or Opinion), tags, the strip's four viewpoints, reason tiles and narrator lines.
- Every source is labeled "made for this game"; the facts they rest on (recess and attention, recess and behavior, outdoor play and activity, school gardens and vegetables) are real and listed in Sources.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Packing an unflipped card plays "Flip it first. Who made it?" and leaves it on the shelf.
- A pocket can be emptied by tapping the source in it.
- Keyboard: Tab through cards and sentences; Enter to flip or pick up; arrow keys choose a pocket or tray; Enter to drop.
- With Motion off cards turn over without spinning and meters jump to their value.

## Look
- Accent `--brand` #8a4b08 scout amber (header, card backs, pockets); gold #f4c542 (the lit strip figure, the picked-up card); paper #fbf6ee; ink #2a1702; muted #5e5446.
- Contrast (WCAG 2.1, computed): white on brand 6.79:1; brand on paper 6.32:1; ink on paper 15.97:1; muted on paper 6.89:1; ink on gold 10.57:1.
- Never color alone: Fact and Opinion trays carry the words and icons (a checkmark magnifier, a thought bubble); meters show numbers.
- Different from this batch (revolution navy, rights plum, change teal, Pony Express saddle rust).

## Art
- People art goes to Gemini with `people: true`: the eight source makers for the recess shelf (the doctor, a parent, the Zoom Toys mascot kid, Principal Ruiz, Mr. Bell, Jayden, a researcher, the nurse; 1 each, cutout yes) and the four strip figures as a set (1 sheet).
- Local FLUX (`scripts/localart.py`): the scout's corner with the shelf (1, 16:9); the source objects (8, 1:1: article page, survey sheet, ad flyer, letter, laptop blog, poster, report cover, log book); the garden shelf objects (8, 1:1).
- Drawn in code: the clipboard, backpack pockets, tags, trays, meters.
About 26 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the narrator and source reader; `playful-friend` as Jayden reading his own poster. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `flip`: "Tap a source to flip it."
- event, whole, each card's back.
- how `pack`: "Drag a flipped source into a pocket."
- how `check`: "Tap Check my pack."
- event, whole, the pack verdict.
- how `sort`: "Drag each sentence to Fact or Opinion."
- event, whole, the sort hint.
- how `trust`: "Pick a reason for this source's trust meter."
- event, whole, the ad aha.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: flip cards with tags, the pack and viewpoint strip, the Fact or Opinion sort, trust meters from three inputs.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pack | Pack the first four cards | The first four are the doctor, the survey, the ad and the principal; the strip shows kids and teachers unlit and the check asks for a swap if no second side. |
| Pack | Pack without flipping | Unflipped cards can't be packed. |
| Sort | Put everything in Fact | Wrong drops play the hint and return; the meter waits until every sentence is sorted. |
| Trust | Pick any reason | The reason shows beside the meter; for the ad, "made by an expert" plays "Who made this? Look at the tag." |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `flip`.
2. Card backs (whole), each waits. `pack`, `check`; verdict (whole).
3. `sort`; hints (whole). `trust`; ad aha (whole).
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D1.5.3-5, D3.1.3-5 and D3.2.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Recess helps children's attention and classroom behavior | American Academy of Pediatrics, "The Crucial Role of Recess in School" (policy statement, Pediatrics, 2013) | CDC and SHAPE America, "Strategies for Recess in Schools" (2017) | yes |
| Classes with daily recess had better teacher-rated behavior than classes with little or none | Barros, Silver and Stein, "School Recess and Group Classroom Behavior," Pediatrics (2009) | AAP 2013 policy statement, which cites it | yes |
| Children are more physically active outdoors than indoors | CDC, "Strategies for Recess in Schools" (2017) | Gray et al., "What is the relationship between outdoor time and physical activity?" Int. J. Environ. Res. Public Health (2015) | yes |
| School gardens are linked to children eating more vegetables | USDA Food and Nutrition Service, Farm to School, "Gardens" | Savoie-Roskos et al., review of garden interventions, J. Acad. Nutr. Diet. (2017) | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-09): the parent survey adds to 41 + 12 + 7 = 60; the first four shelf cards leave kids and teachers unlit; every viewpoint can be lit by exactly one shelf source; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 shelf, backpack and strip fit; at 680x425 the shelf scrolls in one row.
2. Packing lights the strip for each viewpoint; a one-sided pack asks for a swap. (D1.5.3-5)
3. An unflipped card can't be packed; every card's tag shows maker, date, purpose and kind. (D3.1.3-5)
4. The Fact or Opinion sort checks each sentence. (D3.2.3-5)
5. The ad's true fact still gets a low meter and a link to a second source. (D3.2.3-5)
6. The Garden question loads its own eight sources.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no spinning or sliding; no network requests.

## Open questions
None.
