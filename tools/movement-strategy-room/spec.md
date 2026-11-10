# Movement Strategy Room

## One idea
The student sits in the planning rooms of three real campaigns told in order: a church basement in Montgomery, Alabama, on the night of December 1, 1955, after Rosa Parks's arrest; the union hall in Delano, California, in September 1965, when Filipino grape workers led by Larry Itliong walked out and asked Cesar Chavez and Dolores Huerta's farmworkers to join; and the federal building in San Francisco in April 1977, where disabled activists led by Judy Heumann and Kitty Cone sat in to force the government to sign the Section 504 rules; at each branch the student chooses a tactic under real constraints (money, jobs at risk, violence, the law) before a "what they did" card shows the organizers' real choice in their words, and the student's own choice plays forward briefly, labeled as a what-if; tactics carry across campaigns, as the 504 activists learned from earlier sit-ins; at the end an effectiveness board rates each campaign's results (laws, court rulings, public opinion, costs to people), and a then-and-now card shows how the recognized importance of Jo Ann Robinson, Larry Itliong, Dolores Huerta and Brad Lomax has grown as histories were rewritten, so an eleventh grader learns how a person's significance changes over time and context, compares means of changing society and protecting rights, and evaluates how well citizens and institutions addressed problems.

## Not like
- voices-of-freedom (8, spec): primary sources on slavery. Here strategy choices in three campaigns.
- who-decides (12, concept): present-day local action. Here past national campaigns.
- independence-timeline (10, spec): anticolonial paths. Here U.S. rights campaigns.
- levers-of-power (8, spec): one local problem. Here three movements.

## Who and how
- Grade 11, Social Studies (U.S. History and Civics), module "The Civil Rights Movement". Standards: D2.His.3.9-12 (use questions generated about individuals and groups to assess how the significance of their actions changes over time and is shaped by the historical context), D2.Civ.14.9-12 (analyze historical, contemporary, and emerging means of changing societies, promoting the common good, and protecting rights), D2.Civ.5.9-12 (evaluate citizens' and institutions' effectiveness in addressing social and political problems at the local, state, tribal, national, and/or international level).
- Format: story. Driver: one student alone, or small groups planning rival strategies (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three campaigns with about five branches each, what-they-did cards, the effectiveness board, the then-and-now card. Extra: Rival plans (groups plan the same campaign differently and compare with each other and the record). tool.json `modes: ["Planning room", "Rival plans"]`, `minutes: "35-45"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.14.9-12 | At each branch, choose a tactic under real constraints, then compare with the organizers' choice | the tactic cards with costs; the what-they-did card; the what-if line | 2 |
| D2.Civ.5.9-12 | Rate each campaign's results and which institutions (courts, Congress, agencies, companies) acted | the effectiveness board | 3 |
| D2.His.3.9-12 | Write questions about one organizer, then read how their significance was recognized over time | the then-and-now card with dates of recognition | 4 |

## Screens and modes
Header (kit): title "Movement Strategy Room"; `Planning room`, `Rival plans`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A church basement in Montgomery, the night of December 1, 1955: folding chairs, a mimeograph machine, a map of bus routes. A note card: "Rosa Parks, secretary of the local NAACP, was arrested today for refusing to give up her bus seat." The welcome is queued (`welcomeAfter: true`): "Three campaigns, three planning rooms. You choose first; then see what the organizers did. What should happen tomorrow? Tap the map." First hint: "Tap the map of bus routes."

**Campaigns (focus: the room and the choice).** At 1366x768 the room fills the left with tactic cards right; at 680x425 the cards are a sheet. Each branch offers three or four tactics (boycott, carpool, lawsuit, march, sit-in, press, negotiation, fast) with real constraints shown (money, jobs at risk, violence, the law).
1. Montgomery (1955 to 1956): Jo Ann Robinson and the Women's Political Council print tens of thousands of leaflets overnight calling a one-day boycott on December 5; the Montgomery Improvement Association forms with Martin Luther King Jr. as president; a carpool system of hundreds of cars; King's house is bombed (January 1956); boycott leaders indicted under an old anti-boycott law; the lawsuit Browder v. Gayle; the Supreme Court affirms (November 1956); the boycott ends after 381 days and buses ride desegregated on December 21, 1956.
2. Delano (1965 to 1970): Filipino workers of AWOC, led by Larry Itliong, strike on September 8, 1965; the mostly Mexican American NFWA, led by Cesar Chavez and Dolores Huerta, votes to join on September 16; the march to Sacramento (1966); a national grape boycott; Chavez's 25-day fast (1968); contracts with growers (July 1970).
3. The 504 sit-in (1977): Section 504 of the Rehabilitation Act (1973) barred discrimination against disabled people in federally funded programs, but its rules sat unsigned; on April 5, 1977, more than 100 activists occupy the federal building in San Francisco; Deaf, blind and wheelchair-using protesters organize together; the Black Panthers bring meals, a link made by Brad Lomax; Secretary Califano signs the rules on April 28; the sit-in ends after more than 25 days.
- Every "what they did" card quotes the organizers briefly (under 15 words, credited). A student choice that differs plays forward one short what-if, labeled "what might have followed, not what happened."
- Racist and anti-union violence is named plainly (the bombing, arrests, attacks on picket lines) without graphic images.

**The effectiveness board (D2.Civ.5.9-12).** For each campaign the student rates results on four rows (laws and rules, court rulings, public opinion, costs to people) and marks which institutions acted (a federal court, Congress, a federal agency, companies, a city). A note: no campaign won alone; each needed an institution to act.

**Then and now (the aha, D2.His.3.9-12).** The student writes two questions about one organizer (for example "Why was Jo Ann Robinson's role less known for decades?"). The card answers with dates: Robinson's memoir published in 1987; Larry Itliong Day recognized in California in 2015; Dolores Huerta's Presidential Medal of Freedom in 2012; Brad Lomax's role in the 504 sit-in written into histories in recent decades; Judy Heumann's memoir in 2020. Narrator: "Who gets remembered depends on who tells the story, and when."

**The end.** The choices against the record, the board and the then-and-now card. `Print` prints them.

**Rival plans (extra).** Groups plan the same campaign differently and compare with each other and the record.

## Content
- Three campaigns with about fifteen branches, tactic cards with constraints, what-they-did cards with short quotes, what-if lines labeled as such, the board, the then-and-now card.
- All people, events, dates and quotes are real and sourced; the planning-room narrator is not a historical person.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Campaigns go in order; each branch waits for a choice; the record follows.
- Keyboard: Tab to tactic cards, the record, the board and the card; Enter to choose and rate.
- With Motion off cards appear without sliding.

## Look
- Accent `--brand` #1e6045 campaign green (header, tactic cards, the board); gold #f4c542 (the tactic in hand, a rated row); paper #eff6f2; ink #06200f; muted #4d5a52.
- Contrast (WCAG 2.1, computed): white on brand 7.46:1; brand on paper 6.80:1; ink on paper 15.67:1; muted on paper 6.60:1; ink on gold 10.57:1.
- Never color alone: ratings carry words and numbers; institutions carry icons and names.
- Different from this batch (night navy, archive gray, podcast plum, orbit indigo).

## Art
- Public domain or licensed photographs, checked at build (Library of Congress, National Archives, Walter P. Reuther Library, HolLynn D'Lil's 504 photographs with permission): Rosa Parks's booking photograph (1956); a Montgomery carpool; the Delano strike; the march to Sacramento; the 504 sit-in. Each with credit.
- Real faces only for real people. Local FLUX (`scripts/localart.py`): the three empty planning rooms (3, 16:9).
About 8 images.

## Voice
Two bank voices, each unique in this batch: `clear-teacher` as the planning-room narrator and hints; `knowing-guide` as the reader of organizers' words, introduced each time as "from" the speaker, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.campaign + ':' + state.branch + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each branch's situation.
- how `choose`: "Pick a tactic for this moment."
- event, whole, each what-they-did card.
- event, whole, each what-if line.
- how `board`: "Rate each campaign's results."
- how `questions`: "Write two questions about one organizer."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the branching planning rooms, tactic cards, record and what-if cards, the board, the then-and-now card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Branches | Pick at random | Each record card asks which constraint shaped the real choice before the next branch. |
| Board | Rate everything high | Each rating needs one fact from the campaign. |
| Questions | Write yes or no questions | The card checks for a why or how question. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Situation (whole), waits; `choose`; record (whole); what-if (whole).
2. The three campaigns in order.
3. `board`.
4. `questions`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.3.9-12, D2.Civ.14.9-12 and D2.Civ.5.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Parks's arrest (December 1, 1955), Robinson's leaflets, the 381-day boycott, Browder v. Gayle, desegregation December 21, 1956 | Stanford King Institute, "Montgomery Bus Boycott" | Robinson, "The Montgomery Bus Boycott and the Women Who Started It" (Tennessee, 1987) | yes |
| King's house bombed January 1956; leaders indicted under the anti-boycott law | Stanford King Institute | National Archives, Browder v. Gayle records | yes |
| AWOC strike September 8, NFWA joins September 16, 1965; march (1966); fast (1968); contracts (1970) | National Park Service, Cesar E. Chavez National Monument | Walter P. Reuther Library, United Farm Workers collection | yes |
| Larry Itliong's role and California's 2015 recognition | Mabalon, "Little Manila Is in the Heart" (Duke, 2013) | California Legislature, AB 7 (2015) | yes |
| Section 504 (1973); the sit-in from April 5, 1977; rules signed April 28 | U.S. Department of Health and Human Services, Section 504 history | Longmore Institute on Disability, San Francisco State University | yes |
| The Black Panthers fed the sit-in; Brad Lomax's role | Schweik, "Lomax's Matrix," Disability Studies Quarterly (2011) | Heumann, "Being Heumann" (Beacon, 2020) | yes |
| Dolores Huerta's Presidential Medal of Freedom (2012) | Obama White House archives | Dolores Huerta Foundation | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: racist and anti-union violence and segregation are named plainly without graphic images; real faces only; what-if lines are labeled so and never put words in real people's mouths. A fresh-agent read of the branches and record cards is needed before build.

Checks run (Python, scratchpad r19, 2026-11-09): December 5, 1955 to December 20, 1956 (the boycott's last day) is 381 days; April 5 to 28, 1977 is 23 days to the signing; campaigns in date order; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 room and cards; at 680x425 sheet.
2. Each branch's choice is followed by the real choice and a labeled what-if. (D2.Civ.14.9-12)
3. The board rates results and names the institutions that acted. (D2.Civ.5.9-12)
4. Two questions about an organizer get dated recognition answers. (D2.His.3.9-12)
5. Tactics carry across campaigns, noted on the 504 cards.
6. Rival plans compares group plans with the record.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
- Sensitivity flag: racist violence, segregation and anti-union violence (default used: named plainly without graphic images, real faces only, what-ifs labeled and never voiced as real people, fresh-agent read before build).
