# Weekend Substance Choices

## One idea
A phone lock screen lights up with Friday's group chat, and the student lives one weekend as Riley, a made-up high school junior (labeled "illustration"), through three scenes where alcohol, vapes and cannabis edibles show up: a Friday party where someone hands Riley a cup and a vape goes around, a Saturday night when a friend who has been drinking offers a ride home, and a Sunday sleepover where a friend says the edible "isn't working yet" and reaches for another; each scene stops at a decision, the student picks words and an action using a short decision process (what are my choices, what could happen, what matters to me), and three panels update: the body panel shows what the substance does with real timing (an edible can take 30 minutes to 2 hours to kick in, so a second one stacks), the law panel shows that alcohol, tobacco and nicotine, and cannabis are illegal under 21 everywhere in the US and that impaired driving is a crime, and the friendship panel shows how friends react; late Sunday a friend can't be woken and is breathing slowly, and the student checks the danger signs, rolls her onto her side, stays with her and calls 911, and learns that many states protect people who call for help; at the end a weekend map shows each decision and its effects, and that saying no and getting help were real choices at every point, so a student in grades 9 to 12 learns the effects, laws, influences and decisions about alcohol, vaping, cannabis and other drugs.

## Not like
- pressure-point (Grades 6-8, spec): inner thoughts under peer pressure. Here a weekend of decisions with body, law and friend effects.
- captain-s-choices (Grades 9-12, spec): team culture. Here substance choices.
- mind-map (Grades 9-12, live): mental health. Here alcohol, vaping and cannabis.
- recess-upstander (Grades 3-5, spec): bystander moves. Here getting help in an emergency.

## Who and how
- Grades 9-12, Health, module "Alcohol, Drugs and Tobacco". Standards: NHES.S1 (functional health information), NHES.S4 (interpersonal communication), NHES.S5 (decision-making), NHES 3rd edition (2024); CASEL Responsible Decision-Making (anticipating and evaluating the consequences of one's actions).
- Format: story. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every message and panel. Controls 48 px or more.
- Three scenes, six decision points, three effect panels, the help-a-friend sequence, the weekend map. Extra: Class pause (the class votes each decision on the projector). tool.json `modes: ["Weekend", "Class pause"]`, `minutes: "25-35"`, `grades_label: "Grades 9-12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NHES.S1 | Read the body panel at each decision | real timings and risks | 2 |
| NHES.S5 | Use the three-question process; weigh outcomes | the weekend map | 2 |
| NHES.S4 | Pick refusal words; call 911 | friends' reactions; the call | 3 |
| CASEL Responsible Decision-Making | Weigh effects on self, friends and others on the road | the ride decision | 4 |

## Screens and modes
Header (kit): title "Weekend Substance Choices"; `Weekend`, `Class pause`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A phone lock screen with Friday's group chat. The welcome is queued (`welcomeAfter: true`): "Your weekend starts now. Tap the chat to open it." First hint: "Tap the chat."

**Scene (focus: the story).** At 1366x768 the scene is left with the three panels right; at 680x425 the panels are tabs. Each decision shows the three questions, then word and action choices (including saying no, leaving, texting a parent for a pickup code word).

**Panels.** Body: what happens, when, and how long. Law: the age rule and driving rules, with "laws vary by state" where they do. Friendship: how each friend reacts, including friends who back the student up.

**Help a friend.** A check of danger signs (won't wake, slow or uneven breathing, vomiting while passed out, cold or bluish skin); the student rolls her onto her side, stays, and taps `Call 911`; a dispatcher's questions play.

**Real choices (the aha).** Narrator: "Every point had a no, and every point had a way to get help. You used them."

**The end.** The weekend map. `Print` prints it and a danger-signs card.

**Class pause (extra).** Class votes.

## Content
- No brands, no glamour; scenes are grounded and the teens are labeled "illustration".
- Teacher notes name the topics (alcohol, cannabis, vaping, alcohol poisoning), say the tool never asks students about their own use, and list where to send a student who wants help (the school counselor, SAMHSA's helpline 1-800-662-4357, 911 in an emergency).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Any decision can be replayed; the map keeps the last choice and shows replays.
- Keyboard: Tab to messages, decision choices, panels, danger signs and Call 911; Enter picks.
- With Motion off scenes change without slides.

## Look
- Accent `--brand` #34307a late-night indigo (header, the phone frame, buttons); gold #f4c542 (the decision in focus, help actions); paper #f1f0f8; ink #110f2a; muted #514f5e.
- Contrast (WCAG 2.1, computed): white on brand 11.35:1; brand on paper 10.03:1; ink on paper 16.49:1; muted on paper 7.06:1; ink on gold 11.47:1.
- Never color alone: danger signs carry icons and words; panels carry titles.
- Different from this batch (clipboard teal, ski-lift red, pitch-fair green, crayon magenta).

## Art
- People (illustrated): Riley and five friends, a dispatcher's voice card, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): three scenes (3, 16:9), grounded and non-glamorous, no product brands.
- Drawn in code: the phone, panels, the map and the danger-signs card.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Riley's friends; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.scene + ':' + state.decision + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `chat`: "Tap the chat."
- how `think`: "Tap each question, then pick what you do."
- how `panel`: "Tap a panel to read it."
- how `signs`: "Check each danger sign."
- how `call`: "Tap Call 911."
- event, whole, real choices.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the scene graph with decisions, panel content per choice, the help sequence, the weekend map.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Decisions | Pick the first choice | Each decision needs the three questions first. |
| Help | Let her sleep it off | The scene stops and shows why; the student must act. |
| Panels | Skip them | The map shows only the panels read. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `chat`; `think`.
2. `panel`.
3. `signs`; `call`.
4. Real choices (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NHES 2024 S1, S4 and S5 wording; CASEL Responsible Decision-Making | data/standards/nhes-2024.txt | data/standards/casel-5.txt and data/modules.csv | yes |
| Edibles can take 30 minutes to 2 hours to take effect | Centers for Disease Control and Prevention, "Cannabis Facts and Stats" and edibles guidance | National Institute on Drug Abuse, "Cannabis (Marijuana)" DrugFacts | yes |
| Alcohol poisoning signs and what to do (side position, stay, call 911) | National Institute on Alcohol Abuse and Alcoholism, "Understanding the Dangers of Alcohol Overdose" | Centers for Disease Control and Prevention, "Alcohol Poisoning" | yes |
| Under 21 is illegal for alcohol and tobacco nationwide; cannabis under 21 is illegal in every state | National Minimum Drinking Age Act (1984) and FDA, "Tobacco 21" (2019) | National Conference of State Legislatures, state cannabis laws (dated) | yes |
| Many states protect people who call for help in an overdose | National Conference of State Legislatures, "Drug Overdose Immunity and Good Samaritan Laws" | U.S. Government Accountability Office (2021), GAO-21-248, Good Samaritan laws | yes |
Backed twice: 5. Cut: 0.

Sensitivity: alcohol, cannabis, vaping and alcohol poisoning; teacher notes name them; a fresh-agent sensitivity review is owed before Live.

Checks run (Python, scratchpad s27, 2026-11-10): the edible timeline puts a second dose at 45 minutes inside the 30 minute to 2 hour window; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and panels; at 680x425 panels as tabs.
2. Six decisions are made with the three questions and the body panel read. (NHES.S1, NHES.S5)
3. Refusal words are used and 911 is called with the friend on her side. (NHES.S4)
4. The ride decision names effects on others on the road. (CASEL Responsible Decision-Making)
5. No brands; laws are dated with "varies by state" where they vary.
6. `Read` reads every message and panel; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no slides; no network requests.

## Open questions
- Good Samaritan law coverage, which differs by state (default used: "many states" with NCSL and GAO-21-248 dated, and a link card for the student's own state; refresh at Build).
