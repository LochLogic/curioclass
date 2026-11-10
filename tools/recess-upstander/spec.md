# Recess Upstander

## One idea
A playground seen from above has a four-square court, a climbing dome and a strip across the top for one school week, Monday to Friday, and the child stands by the four-square court as a bystander, with all the kids made up and labeled "illustration"; on Monday two kids argue and one shoves over the ball, then they make up, and the child checks the three signs of bullying (on purpose, again and again, one side has more power) and decides it was a conflict; from Tuesday to Friday the same girl, Jada, is left out of four-square, then teased about her shoes, then has her snack taken, and each day the child picks one upstander move, says stop, invites Jada to play, walks her away, or tells the recess aide, puts it in words from a word bank, and sees what the other bystanders do the next day, join in, stay quiet, or step up too; telling the aide is shown as a strong move, not tattling, and the aide's response is shown; no move ever means hitting back; on Friday the child writes one change to ask the principal for, a buddy bench or a game rotation rule, and sees the next week's recess with it; at the end the child sees that one upstander makes it easier for others to step up, and that bullying stops faster when adults know, so a student in grades 3 to 5 learns to tell bullying from conflict, use upstander moves and get adult help.

## Not like
- friend-moves-practice (K, spec): friend moves for young kids. Here bullying and bystanders.
- conflict-coach (Grades 6-8, live): working through a conflict. Here telling conflict from bullying.
- pressure-point (Grades 6-8, spec): inner thoughts under pressure. Here a week of choices at recess.
- parachute-teamwork (K, spec): group games. Here standing up for a classmate.

## Who and how
- Grades 3-5, Health, module "Bullying and Upstanders". Standards: NHES.S4 (interpersonal communication), NHES.S8 (advocacy), NHES 3rd edition (2024); CASEL Relationship Skills (standing up for the rights of others; seeking or offering support and help).
- Format: roleplay. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five days, the three-sign check, four upstander moves with a word bank, bystander reactions, the Friday ask. Extra: Class circle (the class picks Friday's change together on the projector). tool.json `modes: ["Recess week", "Class circle"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NHES.S4 | Pick a move and say it in words; tell the aide | others stepping up; the aide responding | 3 |
| NHES.S8 | Ask the principal for a change | next week's recess | 4 |
| CASEL Relationship Skills | Check the three signs; support Jada safely | conflict versus bullying | 2 |

## Screens and modes
Header (kit): title "Recess Upstander"; `Recess week`, `Class circle`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The playground from above, the week strip, and the child's marker by four-square. The welcome is queued (`welcomeAfter: true`): "Watch recess. You're standing by four-square. Tap Monday." First hint: "Tap Monday."

**Monday (focus: the playground).** At 1366x768 the playground is left with the day card right; at 680x425 the card is a sheet. The shove plays; three sign checkboxes; the child decides conflict or bullying and hears why.

**Tuesday to Friday.** Each day's moment plays; the child picks a move and builds its words from a word bank ("Stop. That's not okay." "Jada, come play with us."). The next day opens with the bystanders' reaction.

**The aide.** Telling the aide shows the aide listening, thanking the child and checking on Jada.

**Friday ask.** The child picks or writes one change and sees next week's recess.

**One makes room for more (the aha).** Narrator: "You stepped up, and others followed. And the grown-ups knew, so it stopped."

**The end.** The week strip with moves and reactions, and the Friday ask. `Print` prints them.

**Class circle (extra).** Class choice.

## Content
- Pushing is shown as a ball knocked away, never an injury; faces are readable.
- Teacher notes: a short guide on what to do if a student shares that they are being bullied (listen, thank them, tell the school counselor), and that the tool never asks children about their own experiences.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A day can be replayed with a different move; the week keeps the last choice.
- Keyboard: Tab to days, sign checkboxes, moves, word bank chips and the ask; Enter picks.
- With Motion off each moment shows as three still frames.

## Look
- Accent `--brand` #a2470d playground orange (header, the week strip, buttons); gold #f4c542 (the child's marker, the day in focus); paper #fdf2ea; ink #2c1203; muted #5e4e44.
- Contrast (WCAG 2.1, computed): white on brand 6.10:1; brand on paper 5.54:1; ink on paper 15.96:1; muted on paper 7.20:1; ink on gold 10.81:1.
- Never color alone: signs are checkboxes with words; reactions carry icons and words.
- Different from this batch (range sage, parachute red, fridge blue, gym purple).

## Art
- People (illustrated): Jada, the teasing kids, bystanders and the aide, labeled "illustration" (Gemini, `people: true`, 8; cutout yes).
- Local FLUX (`scripts/localart.py`): the playground from above (1, 16:9), the buddy bench (1, 4:3).
- Drawn in code: the week strip, day cards, checkboxes and the word bank.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `clear-teacher` as the recess aide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `day`: "Tap the next day."
- how `signs`: "Check the signs, then tap conflict or bullying."
- how `move`: "Pick a move."
- how `words`: "Pick words from the word bank."
- how `ask`: "Pick a change to ask for."
- event, whole, one makes room for more.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the week with day moments, sign checks, moves with word banks, bystander reaction rules, the Friday redraw.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Signs | Call everything bullying | Monday's shove has only one sign and is checked. |
| Moves | Do nothing all week | Bystanders join in, and the end asks for a move and the aide. |
| Words | Pick a mean line | The word bank has only safe words; the move needs a full line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `day`; `signs`.
2. `move`; `words`.
3. `ask`.
4. One makes room for more (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NHES 2024 S4 and S8 wording; CASEL Relationship Skills | data/standards/nhes-2024.txt | data/standards/casel-5.txt and data/modules.csv | yes |
| Bullying is unwanted, aggressive, repeated or likely to repeat, with a power imbalance | Centers for Disease Control and Prevention (2014), "Bullying Surveillance Among Youths: Uniform Definitions" | StopBullying.gov, "What Is Bullying" | yes |
| When peers step in, bullying often stops quickly | Hawkins, Pepler and Craig (2001), "Naturalistic observations of peer interventions in bullying", Social Development | StopBullying.gov, "The Roles Kids Play" and bystander guidance | yes |
| Telling an adult is a key step, not tattling | StopBullying.gov, "How to Prevent Bullying" for kids | American Academy of Pediatrics, HealthyChildren.org, "Bullying: It's Not OK" | yes |
Backed twice: 4. Cut: 0.

Sensitivity: bullying and pushing; teacher notes name it and cover disclosure; a fresh-agent sensitivity review is owed before Live.

Checks run (Python, scratchpad s26, 2026-11-10): four days of teasing after one conflict day meets "again and again" from Wednesday on; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 playground and card; at 680x425 card as a sheet.
2. Monday is judged a conflict from the three signs. (CASEL Relationship Skills)
3. Four days get an upstander move in words, including telling the aide. (NHES.S4)
4. A Friday change is asked for and shown. (NHES.S8)
5. No injuries; teacher notes cover disclosure.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames; no network requests.

## Open questions
None.
