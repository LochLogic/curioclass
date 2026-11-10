# Bill to Law Board Game

## One idea
The child carries a bill that kids proposed around a board shaped like a state capitol: first the real story of New York's fourth graders who got yogurt named the official state snack in 2014 (a sponsor files it, a committee hears it, both chambers vote, the governor signs), then a made-up bike lane bill from Ms. Nakamura's fourth graders that meets a cost estimate, an amendment, a governor's veto and an override vote; role cards say what legislators, the governor and the courts can and can't do, a constitution card shows where the board's rules come from, and a split board sorts powers between the U.S. Constitution and the state constitution, so a fourth grader learns how a state law is made, who holds which power, and how people (kids too) change laws and how laws change daily life.

## Not like
- checks-and-balances (12, concept, same family): the federal branches checking each other at grade 12. Here one state bill's path at grade 4.
- pool-repair-vote (3, spec): a town council's choice. Here a state legislature and governor.
- promise-check (3, spec): what each office can promise. Here how a bill moves through the offices.
- town-council (2, spec): one meeting. Here a whole process across months.

## Who and how
- Grade 4, Social Studies (Civics), module "State Government". Standards: D2.Civ.1.3-5 (distinguish the responsibilities and powers of government officials at various levels and branches of government and in different times and places), D2.Civ.5.3-5 (explain the origins, functions, and structure of government with reference to the U.S. Constitution, state constitutions, and selected other systems of government), D2.Civ.12.3-5 (explain how rules and laws change society and how people change rules and laws).
- Driver: one child alone (tool.json `driver: "student"`); class teams in the extra. `Read` reads every card. Controls 44 px or more.
- Two bills in order (the real one first), the constitution card and the powers sort along the way. Extra: Rival bills (two teams on one board). tool.json `modes: ["Yogurt bill", "Bike lane bill", "Rival bills"]`, `minutes: "25-35"`, `grades_label: "Grade 4"`.
- Family: bill-to-law (shared with checks-and-balances). No engine doc exists yet; this spec names the parts a shared engine would hold.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.1.3-5 | On each space, play the right role card (legislator, committee chair, governor, court) and see what it can and can't do | the role cards with "can" and "can't" lines; a wrong card says why | 2 |
| D2.Civ.5.3-5 | Open the constitution card at the start; sort six powers onto the split board (U.S. Constitution, state constitution, both) | the constitution card (origin, three branches, Nebraska's one chamber); the split board | 3, 4 |
| D2.Civ.12.3-5 | Follow the yogurt bill from kids' letters to law; in the bike lane bill, gather support and win the override; read the "after" screens | the board path, support cards, vote counts, and an after screen of daily life | 5, 6 |

## Screens and modes
Header (kit): title "Bill to Law Board Game"; `Yogurt bill`, `Bike lane bill`, `Rival bills`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A board drawn like a capitol from above: a left wing (Senate), a right wing (Assembly or House), the governor's office at the top of the dome, a courts building across the plaza, and a path of spaces winding through them. A rolled-up paper sits on the start space. The welcome is queued (`welcomeAfter: true`): "Laws can start with kids! In 2014 a class of fourth graders in New York had an idea. Tap the paper to read their bill." First hint: "Tap the paper."

**Constitution card (first).** Before the first move: "Every state has its own constitution. It says how the state's government works. Like the U.S. Constitution, it sets up three branches: a legislature makes laws, a governor carries them out, and courts decide what laws mean." A tap shows New York's first constitution (1777) and that 49 states have two chambers, while Nebraska has had one since 1937.

**Yogurt bill (the real story, focus: the board and the step card).** At 1366x768 the board fills the screen with the step card right; at 680x425 the step card opens as a sheet after each move.
- The child taps `Move` to go one space; each space plays its step and asks for a role card:
  1. Idea: the class studies New York's government and farming, learns the state is a top yogurt maker, and writes over 200 letters to lawmakers, farms and yogurt companies.
  2. Sponsor: a state senator and an assembly member agree to sponsor and file the bill (S.6695 in the Senate). Role card: Legislator ("can write and file bills; can't make a law alone").
  3. Committee: a committee hears the bill and votes to send it on. Role card: Committee chair.
  4. Senate vote: passes 52 to 8. A chance card: "Some senators joke and argue in a late-night debate. A bill can be talked about a lot, even a small one."
  5. Assembly vote: passes.
  6. Governor: signs on October 15, 2014. Role card: Governor ("can sign or veto bills; can't write them").
- After screen: yogurt is New York's official snack; the class visits Albany; dairy farms in the state are named in the narrator's line ("New York's dairy farmers make a lot of yogurt. Now the whole state knows it."). Narrator: "Kids had an idea, wrote letters, found sponsors and followed it all the way."

**Bike lane bill (made up, focus: the board, support cards and votes).** Ms. Nakamura's fourth graders want painted bike lanes near every school. The same board, labeled State Senate and State House. Support cards collect in a tray:
  1. Sponsor files the bill.
  2. Committee hearing: testimony cards (a bike shop owner and a parent support it; a town road chief worries about cost). A cost estimate says $20 million. The child may play `Amend` to start with 100 schools (cost $5 million); it earns a support card.
  3. Kids' letters space: the child may write a letter from tiles (who we are, what we want, why) for another support card.
  4. House vote and Senate vote: counts depend on support cards (with both: House 68 of 100, Senate 24 of 35; with one: 63 and 22; with none: 58 and 19). The bill passes both with any count over half.
  5. Governor: vetoes ("It costs too much this year.").
  6. Override: needs two thirds in both chambers (67 of 100 and 24 of 35). With both support cards it passes; with fewer it fails and the bill dies this session.
- After screen if it passes: painted lanes by schools, more kids biking. If it dies: "Bills that die can come back next year. The class keeps its letters and its amendment and tries again." Either way the narrator names what the class did.
- Role card: Courts ("can decide whether a law follows the constitution if someone challenges it; can't vote on bills"). Played on the courts space, where nothing happens this time: "No one challenged the law. Courts only act when a case comes to them."

**Powers sort (between the bills).** A split board: U.S. Constitution | Both | State constitution. Six power cards: print money (U.S.), make treaties with other countries (U.S.), run public schools (state, with local school districts), issue driver's licenses (state), collect taxes (both), make laws about crimes (both). Wrong drop: "Which constitution gives that power? Think: is it for the whole country or just your state?"

**Rival bills (extra).** Two teams carry two bills on one board with the bike lane rules; the projector shows both tokens.

## Content
- One real bill with six steps and real facts; one made-up bill with seven spaces, three testimony cards, one amendment, one letter, set vote counts and an override; four role cards; the constitution card; six power cards.
- The real class and its students are not named; the sponsors are named as in public records.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Move` shows when the space's step is done. `Amend` shows only at the committee hearing of the bike bill. The override space shows only after a veto.
- Keyboard: Enter for `Move`; Tab through role and power cards.
- With Motion off the token jumps space to space.

## Look
- Accent `--brand` #7b2d3b capitol maroon (header, the path, card frames); gold #f4c542 (the token, a played card, yes votes); paper #faf1f2; ink #260b11; muted #614f53.
- Contrast (WCAG 2.1, computed): white on brand 9.21:1; brand on paper 8.30:1; ink on paper 16.63:1; muted on paper 6.88:1; ink on gold 11.34:1.
- Never color alone: votes show numbers and "Yes" or "No"; role cards have icons and names.
- Different from this batch (inquiry rust, learn-and-earn teal, made-for-whom slate, economy map blue).

## Art
- People art goes to Gemini with `people: true`: Ms. Nakamura and her class (2 scenes, illustrated); a legislator, a committee chair, a governor, a judge (role cards, 1 pose each; generic, not real officials); testimony speakers (3).
- Local FLUX (`scripts/localart.py`): the capitol board from above (1, 16:9); after screens (3: yogurt, bike lanes painted, a class with letters).
- Drawn in code: the path, token, step cards, support tray, vote counts, the split board, the constitution card.
About 15 images.

## Voice
Four bank voices, each unique in this batch: `calm-professor` as the narrator; `bright-teacher` as Ms. Nakamura; `soft-breath` as a student in her class who reads the letter; `firm-captain` as the governor's veto line. `Curio.voice` with `scope: () => state.mode + ':' + state.space + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, the constitution card.
- event, whole, each space's step.
- how `role`: "Play the role card for this step."
- event, whole, each role card's can and can't lines.
- how `move`: "Tap Move."
- how `amend` (once): "Tap Amend to make the bill cost less, or keep going."
- event, whole, vote counts, the veto and the override result.
- how `sort`: "Drag each power to the constitution that gives it."
- event, whole, each after screen.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
bill-to-law (no engine doc; shared with checks-and-balances). This tool adds: a space path with step cards, role cards with can and can't checks, support cards that set vote counts, veto and override rules. Keep the path and vote rules as plain data so checks-and-balances can reuse them with federal branches.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Role cards | Play any card | Each space takes one role; a wrong card reads its "can't" line. |
| Override | Skip the amendment and the letter | The override fails and the bill dies; the after screen says what the class could do next. |
| Powers sort | Put everything in Both | Only two powers are shared; wrong drops ask whole country or just the state. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Constitution card (whole).
2. Each space: step (whole), waits; `role`; card lines (whole); `move`.
3. Bike bill: `amend` once; votes, veto, override (whole).
4. `sort`; after screens (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.1, 5 and 12 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Byron-Bergen Elementary fourth graders proposed yogurt as New York's state snack, sent over 200 letters, and Governor Cuomo signed it on October 15, 2014 | Manufacturing.net, "Yogurt is now official New York state snack" (2014) | New York State Assembly, Assemblyman Stephen Hawley news release on the Byron-Bergen students (2014) | yes |
| The Senate bill, S.6695, passed 52 to 8 | statesymbolsusa.org, New York state snack | Fox News, "New York Senate passes bill making yogurt official state snack" (2014) | yes |
| New York's first constitution was adopted in 1777 | New York State Archives, "New York's constitutions" | Wikipedia, Constitution of New York (checked 2026-11-09) | yes |
| Nebraska has a one-chamber legislature, since 1937 | Nebraska Legislature, "History of the Unicameral" | National Conference of State Legislatures, "Nebraska's unicameral" | yes |
| Most state legislatures need two thirds of each chamber to override a governor's veto | National Conference of State Legislatures, "Veto overrides" | Ballotpedia, "Veto override provisions" | yes |
| The U.S. Constitution gives coining money and treaties to the national government; states run schools and license drivers; both tax | National Archives, U.S. Constitution, Article I sections 8 and 10, Tenth Amendment | Annenberg Classroom (Annenberg Public Policy Center), "Federalism" | yes |
Backed twice: 7. Cut: 0. The bike lane bill, Ms. Nakamura's class and its vote counts are made up.

Checks run (Python, scratchpad r7, 2026-11-09): bike bill votes with 2, 1 and 0 support cards are House 68, 63, 58 of 100 and Senate 24, 22, 19 of 35; all pass by majority; only the 2-card counts reach two thirds (67 and 24); powers sort 2 U.S., 2 state, 2 both; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and step card fit; at 680x425 the step card is a sheet.
2. Each space takes only its role card. (D2.Civ.1.3-5)
3. The constitution card plays first and names the three branches and Nebraska's one chamber. (D2.Civ.5.3-5)
4. Six powers sort to their constitutions. (D2.Civ.5.3-5)
5. The yogurt bill follows its six real steps with the checked facts. (D2.Civ.12.3-5)
6. The bike bill's override passes only with both support cards, and both after screens play. (D2.Civ.12.3-5)
7. `Amend` and the override space are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the token jumps; no network requests.

## Open questions
- None for Cory. (The idea card's "needs a data source" is met by the New York yogurt bill, checked above.)
