# Ripple Street

## One idea
The child makes Ava's five Saturday choices on Ripple Street (rake Mr. Grant's leaves or go to the park, return a late library book or keep reading, plant flowers or play a game, blast music on the porch or wear headphones, leave her bike on the sidewalk or put it away), weighs each on a two-column card (what Ava gets, what she gives up), sees a reward or a fine arrive and decides whether it changes her mind, then watches the ripples spread down the street to the neighbors, so a third grader learns that every choice has costs and benefits, that rewards and fines nudge choices, and that a choice can help or hurt people who didn't make it.

## Not like
- piggy-bank-planner (2, spec): saving toward one goal. Here many small choices and their effects on others.
- smoke-and-honey (6, concept): externalities and the policies that fix them. Here a kid's own day at grade 3.
- pool-repair-vote (3, spec): a town choosing how to pay. Here one kid choosing for herself.
- school-fix-it-meeting (3, spec, this batch): a group decides together. Here one person decides and others feel it.

## Who and how
- Grade 3, Social Studies (Economics), module "Ripple Street". Standards: D2.Eco.1.3-5 (compare the benefits and costs of individual choices), D2.Eco.2.3-5 (identify positive and negative incentives that influence the decisions people make), D2.Eco.8.3-5 (identify examples of external benefits and costs).
- Driver: one child alone, or the teacher on the projector with the class voting each choice (tool.json `driver: "either"`). `Read` reads every line. Controls 44 px or more.
- One day in five choices, then the day's map. Extra: Class votes (each choice shows a quick tally the teacher fills). tool.json `modes: ["Saturday", "Class votes"]`, `minutes: "15-25"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.1.3-5 | For each choice, drag four picture chips into Ava gets / Ava gives up, then pick | the two-column card for each choice | 2 |
| D2.Eco.2.3-5 | When a reward or fine arrives, tag it Reward (positive) or Fine (negative), then decide if Ava switches | the nudge card with its tag and Ava's thought | 3 |
| D2.Eco.8.3-5 | Watch each ripple and tag it Helps a neighbor or Costs a neighbor | ripples on the street map with a plus or minus marker at each house | 4, 5 |

## Screens and modes
Header (kit): title "Ripple Street"; `Saturday`, `Class votes`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Ripple Street at 8 a.m. from above and a little to the side: six houses, a sidewalk, the library at the end, a park across the way. Ava stretches on her porch. The welcome is queued (`welcomeAfter: true`): "It's Saturday on Ripple Street! Ava has choices to make, and you'll help her. Tap Ava to start." First hint: "Tap Ava."

**Saturday (focus: the choice card over the street).** At 1366x768 the street fills the top half and the card sits below; at 680x425 the card opens as a sheet and the street shows only during ripples.
- Each choice runs four beats: two-column card, pick, nudge, ripple.
- The five choices, in clock order:
  1. 9 a.m. Rake Mr. Grant's leaves, or go to the park with friends. Chips: fun with friends, tired arms, time, a clean yard. Nudge: Mr. Grant offers $5 (Reward). Ava's thought if the child picked the park: "Five dollars would help me buy those paints I want." Ripple if raked: the sidewalk is clear, so Mr. Grant can walk safely with his cane (Helps).
  2. 11 a.m. Return the late library book, or keep reading it at home. Chips: finish the story, a walk, the next reader, time. Nudge: the late fee goes up 10 cents every day (Fine). Ripple if returned: Sam, next on the waiting list, gets the book today (Helps). If kept: Sam waits another week (Costs).
  3. 1 p.m. Plant flowers in the window box, or play a video game. Chips: dirty hands, fun on the screen, pretty flowers, time. Nudge: the block club gives a sticker for every new flower box (Reward). Ava's thought: "I'd plant them anyway. I love flowers." (the nudge doesn't change her mind) Ripple if planted: bees visit Mrs. Lin's garden next door, and her tomatoes grow (Helps).
  4. 2 p.m. Play loud music on the porch, or listen with headphones. Chips: loud fun, sore ears, dancing, it's quieter. Nudge: the block club rule says quiet from 1 to 3, and the first time is a warning (Fine). Ripple if loud: the Rossi baby next door wakes up crying, and her dad's nap is over too (Costs). If headphones: the baby sleeps (no ripple).
  5. 5 p.m. Leave her bike on the sidewalk, or put it in the garage. Chips: fast, easy, takes a minute, safe from rain. No nudge here: "No reward, no fine. What will Ava do?" Ripple if left: Mr. Grant has to step into the street to get around it (Costs).
- Each nudge asks: "Is this a reward or a fine?" (tap `Reward` or `Fine`), then "Does it change Ava's mind?" (tap `Switch` or `Stay`). The child decides; Ava says her thought either way.
- Ripples: a ring spreads from Ava's house to the house it reaches, which gets a plus (green ring and the word "Helps") or a minus (orange ring and the word "Costs"). The child taps `Helps` or `Costs` to tag it before the word shows.

**The day's map (end state).** Two columns over the evening street: Ava's tally (what she got, what she gave up, for each choice) and the street's ripples (each neighbor with a plus or minus). The narrator: "Some choices were good for Ava and good for the street. Some were good for Ava but cost a neighbor. Which choice would you change?" The child taps a choice to replay just that one. `Print` prints the day's map.

**Class votes (extra).** Each choice shows the two options as big buttons; the teacher enters a show-of-hands count; the tool plays the majority choice and its ripple.

## Content
- Five choices, each with four chips (two per column, one possible either way), four nudges (two rewards, two fines), and up to two ripples each (one per option).
- Neighbors: Mr. Grant (older, walks with a cane), Sam (a kid on the library waiting list), Mrs. Lin (gardener), the Rossi family (a baby and her dad).
- Ripple Street and everyone on it are made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Reward`, `Fine`, `Switch` and `Stay` show only after a nudge appears. `Helps` and `Costs` show only during a ripple.
- Keyboard: Tab to a chip, Enter to pick up, arrow keys between columns, Enter to drop.
- With Motion off ripples appear as still rings.

## Look
- Accent `--brand` #1f5f8b ripple blue (header, card frame, rings' outline); gold #f4c542 (the active chip, Ava's marker); paper #eff5fa; ink #0a1f2e; muted #4d5a64.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.23:1; ink on paper 15.31:1; muted on paper 6.45:1; ink on gold 10.34:1.
- Never color alone: ripple rings carry "Helps" with a plus or "Costs" with a minus.
- Different from this batch (fix-it plum, barter ochre, skateboard berry, valley olive).

## Art
- People art goes to Gemini with `people: true`: Ava (4 poses: stretching, raking, planting, dancing; cutout yes); Mr. Grant, Mrs. Lin, Sam, Mr. Rossi with the baby (1 pose each; cutout yes).
- Local FLUX (`scripts/localart.py`): Ripple Street from above (2: morning and evening, 16:9, same framing); chip pictures (14, 1:1).
- Drawn in code: the cards, nudge cards, ripple rings, markers, the day's map.
About 24 images.

## Voice
Three bank voices, each unique in this batch: `upbeat-guide` as the narrator; `playful-friend` as Ava; `warm-teacher` as the neighbors' lines. `Curio.voice` with `scope: () => state.mode + ':' + state.choice + ':' + state.beat`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `chips`: "Drag each picture to Ava gets or Ava gives up."
- how `pick`: "Now tap what Ava should do."
- event, whole, each nudge.
- how `tag`: "Is this a reward or a fine? Tap one."
- how `mind`: "Does it change Ava's mind? Tap Switch or Stay."
- event, whole, Ava's thought (Ava's voice).
- how `ripple`: "Does this help the neighbor or cost them? Tap Helps or Costs."
- event, whole, each ripple line.
- event, whole, `map`: as in the end state.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the two-column chip sort, the nudge card, the ripple rings and the day's map.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Two columns | Drop all chips in one column | Each column takes two; wrong drops return. |
| Reward or Fine | Tap Reward each time | Two nudges are fines; a wrong tag replays the nudge. |
| Helps or Costs | Tap Helps each time | Three of the possible ripples are costs; a wrong tag replays the ripple. |
| Switch or Stay | Any tap | Both are fine; the lesson is Ava's thought and the ripple. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each choice: `chips`; `pick`.
2. Nudge: the nudge (whole), waits; `tag`; `mind`; Ava's thought (whole).
3. Ripple: the ripple line (whole); `ripple`.
4. End: `map` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.1, D2.Eco.2 and D2.Eco.8 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Every choice has a cost (what you give up) and a benefit | Federal Reserve Bank of St. Louis, Econ Lowdown, "Opportunity cost" | Council for Economic Education, Voluntary National Content Standards in Economics, Standard 1 | yes |
| Rewards are positive incentives and fines or penalties are negative incentives | Federal Reserve Bank of St. Louis, Econ Lowdown, "Incentives" | Council for Economic Education, Voluntary National Content Standards in Economics, Standard 4 | yes |
| An external benefit or cost falls on people who didn't make the choice (bees from a garden, noise) | Econlib, "Externalities" (Concise Encyclopedia of Economics) | Federal Reserve Bank of St. Louis, Page One Economics, "Externalities" | yes |
| Bees visiting flowers help pollinate nearby vegetable gardens | USDA, "Pollinators" | U.S. Fish and Wildlife Service, "Pollinators" | yes |
| Many U.S. libraries still charge late fines while others have dropped them | American Library Association, resolution on monetary library fines (2019) | Wikipedia, Library fine (checked 2026-11-09) | yes |
Backed twice: 6. Cut: 0. Ripple Street, its people and the block club rule are made up.

Checks run (Python, scratchpad r6, 2026-11-09): five choices each have four chips split two and two; nudges are two rewards and two fines; across both options there are three Helps ripples and three Costs ripples; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 street and card fit; at 680x425 the card is a sheet.
2. Each choice's chips land in the right columns. (D2.Eco.1.3-5)
3. Each nudge is tagged right, and Ava's thought plays after Switch or Stay. (D2.Eco.2.3-5)
4. Each ripple reaches the right house and takes its right tag. (D2.Eco.8.3-5)
5. The day's map shows Ava's tally beside the street's ripples, and a single choice replays. (D2.Eco.8.3-5)
6. `Reward`, `Fine`, `Switch`, `Stay`, `Helps` and `Costs` are never named before they show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still rings; no network requests.

## Open questions
- None for Cory.
