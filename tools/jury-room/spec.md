# Jury Room

## One idea
The student takes seat 7 on a twelve-person civil jury in a made-up case: a small bakery says a delivery company's driver dropped and broke its new oven and wants the company to pay; the binder holds photographs of the crate, the delivery log with time stamps, the driver's statement and a neighbor's statement, and the judge's instruction says the bakery must prove its case by a preponderance of the evidence (more likely than not); eleven illustrated jurors each bring evidence they noticed, a bias and a habit (one talks over others, one stays quiet but saw the key time stamp, one decided in the first minute), and each round the student chooses how to act (ask the quiet juror, cite an exhibit, name an assumption, propose a vote, sum up where the room stands) while a deliberation meter tracks whether every voice and every exhibit was heard; snap judgments (about the driver's accent, about a big company) appear and the student can name and test them against the evidence; after the verdict the turning points replay, then the same dispute goes to a town hall decided by majority vote and to a consensus circle, and the student compares what each process is good for, so a twelfth grader learns to apply civic virtues and democratic principles when working with others, to use fitting deliberative processes in different settings, and to collaborate by drawing out other voices and building a shared decision.

## Not like
- supreme-court-simulator (12, spec): justices ruling on law. Here jurors weighing facts.
- who-decides (12, spec): addressing a public body. Here deciding inside one.
- build-a-government (12, spec): designing institutions. Here working inside one.
- case-conference (12, concept): a team on a psychology case. Here a jury on a civil case.

## Who and how
- Grade 12, Social Studies (Government), module "Jury Room". Standards: D2.Civ.7.9-12 (apply civic virtues and democratic principles when working with others), D2.Civ.9.9-12 (use appropriate deliberative processes in multiple settings), AASL.Collaborate (AASL III.A.3, deciding to solve problems informed by group interaction; III.C.2, involving diverse perspectives in their own inquiry processes; III.D.1, actively contributing to group discussions).
- Format: roleplay. Driver: one student alone with eleven computer jurors, or twelve students with role cards (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- About eight deliberation rounds, four exhibits, eleven jurors, the verdict and replay, the town hall and the consensus circle, the comparison. AASL.Collaborate is simulated in solo play; the class mode makes it real. Extra: Twelve seats (each student takes a juror's role card). tool.json `modes: ["Seat 7", "Twelve seats"]`, `minutes: "35-45"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.7.9-12 | Each round, choose an action that listens, cites evidence or tests a bias | the action cards; jurors' responses; the bias check | 2, 3 |
| AASL.Collaborate (III.A.3, III.C.2, III.D.1) | Draw out the quiet jurors and build on others' points before the vote | the deliberation meter's voices row | 2 |
| D2.Civ.9.9-12 | Run the same dispute through a town hall and a consensus circle and compare | three process cards with outcomes; the comparison | 4 |

## Screens and modes
Header (kit): title "Jury Room"; `Seat 7`, `Twelve seats`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A jury room: a long table with twelve chairs, the student's at seat 7; the evidence binder; a whiteboard; the judge's instructions on a card. The case is labeled "made up for this game". The welcome is queued (`welcomeAfter: true`): "Eleven people, one decision, and you're one of them. Everyone has to be heard before you vote. Open the judge's instructions." First hint: "Tap the judge's instructions."

**Deliberation (focus: the table).** At 1366x768 the table fills the left with the action cards and meter right; at 680x425 the cards are a sheet. Each round a juror speaks, then the student picks one action:
- Ask a juror (especially one who hasn't spoken).
- Cite an exhibit (the crate photographs show a forklift scrape; the log shows the drop-off at 2:14 p.m. and the bakery's call at 2:52 p.m.; the driver says the crate was already scraped; the neighbor saw the crate tip off the lift gate).
- Name an assumption ("Are we deciding because of his accent, or the log?").
- Propose a vote, or sum up where the room stands.
- The meter has two rows: voices heard (each juror who spoke and was answered) and exhibits used. Jurors respond to the student's choice by stated rules.

**Bias checks (D2.Civ.7.9-12).** Snap judgments appear as thought cards over jurors ("Drivers are always careless", "Big companies can afford it", "His accent makes him hard to trust"). The student can name a judgment and test it against an exhibit; the juror updates or holds.

**Verdict and replay.** A unanimous verdict is needed (the judge's instruction says so for this made-up court). The replay shows the turning points: who spoke when, which exhibit moved whom. The evidence is built so a careful room finds the company more likely than not responsible, but a split is possible if exhibits are skipped.

**Other processes (the aha, D2.Civ.9.9-12).** The same dispute goes to a town hall (a show of hands, majority wins; quick, but the quiet neighbor's sighting never comes up) and a consensus circle (everyone speaks in turn and the group shapes an outcome all can accept; slower, with a repair plan instead of a verdict). The student compares: "A jury is right for ___ because ___. A town hall fits ___. A circle fits ___." Narrator: "How a group decides changes what it hears."

**The end.** The verdict, the meter, the replay and the comparison. `Print` prints them.

**Twelve seats (extra).** Twelve students take role cards (evidence, a bias, a habit) and deliberate for real; the meter is kept by a student recorder.

## Content
- A made-up civil case with four exhibits, judge's instructions, eleven jurors with role cards, stated response rules, the three process scenes, the comparison template.
- Biases shown are named and tested, never endorsed; jurors are varied in age, background and manner without stereotypes.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A vote can be proposed any time, but the verdict needs unanimity; the meter shows who hasn't been heard.
- Keyboard: Tab to jurors, the binder, action cards and the meter; Enter to act.
- With Motion off jurors' cards appear without sliding and the meter jumps.

## Look
- Accent `--brand` #6e3b2e jury brown (header, the table, action cards); gold #f4c542 (the speaking juror, the exhibit cited); paper #f9f2ef; ink #211009; muted #5e5551.
- Contrast (WCAG 2.1, computed): white on brand 9.02:1; brand on paper 8.15:1; ink on paper 16.61:1; muted on paper 6.56:1; ink on gold 11.30:1.
- Never color alone: the meter carries counts and names; bias cards carry an icon and words.
- Different from this batch (court purple, branch amber, campaign blue, charter green).

## Art
- People (illustrated) for eleven distinct jurors and the student's seat, labeled "illustration" (Gemini, `people: true`, 11; cutout yes).
- Local FLUX (`scripts/localart.py`): the jury room (1, 16:9), a town hall (1, 16:9), a circle of chairs (1, 16:9).
- Exhibits drawn in code (the log, the crate diagram).
About 14 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as the jurors' voice, each introduced by seat number and name; `firm-captain` as the judge's instructions, narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.juror + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, the judge's instructions.
- event, whole, each juror's turn.
- how `act`: "Choose how to speak or act."
- how `bias`: "Name the assumption and test it with an exhibit."
- event, whole, the verdict and replay.
- how `compare`: "Compare the three ways of deciding."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the table with juror rules, action cards, the meter, bias checks, the replay, the process scenes.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Deliberation | Propose a vote every round | The room splits until every juror is heard; the quiet juror's time stamp is never raised. |
| Bias | Ignore the thought cards | The juror holding the bias won't move without a test against an exhibit. |
| Comparison | Call the jury best for everything | The comparison asks for a fit for each process. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Judge's instructions (whole).
2. Juror's turn (whole), waits; `act`; `bias` when a thought card appears.
3. Verdict and replay (whole).
4. `compare`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.7.9-12 and D2.Civ.9.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| AASL III.A.3, III.C.2 and III.D.1 wording | AASL, "National School Library Standards" (ALA, 2018) | data/standards/aasl-2018.txt (codes) | yes |
| Preponderance of the evidence in civil cases; jury instructions | U.S. Courts, "Juror Handbook" and "Civil Cases" | Federal Judicial Center, model civil jury instructions | yes |
| Federal civil verdicts are unanimous unless the parties agree otherwise; many states differ | Federal Rules of Civil Procedure, Rule 48 | National Center for State Courts, "State of the States Survey of Jury Improvement Efforts" | yes |
| Evidence-driven and verdict-driven deliberation styles | Hastie, Penrod and Pennington, "Inside the Jury" (Harvard, 1983) | Devine and colleagues, Psychology, Public Policy, and Law (2001) | yes |
| Diverse juries deliberated longer and discussed more facts | Sommers, Journal of Personality and Social Psychology (2006) | American Bar Association, "Principles for Juries and Jury Trials" | yes |
| Consensus and circle processes | U.S. Department of Justice, Office of Justice Programs, circle processes | Pranis, "The Little Book of Circle Processes" (Good Books, 2005) | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r22, 2026-11-09): twelve seats with eleven computer jurors; the bakery's call came 38 minutes after drop-off; every exhibit is needed to reach a unanimous verdict under the stated rules; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and cards; at 680x425 sheet.
2. Every juror is heard and every exhibit used before the verdict opens. (D2.Civ.7.9-12, AASL.Collaborate)
3. Each bias card is named and tested against an exhibit. (D2.Civ.7.9-12)
4. The town hall and consensus circle are run and compared with the jury. (D2.Civ.9.9-12)
5. The case is labeled made up; jurors are varied without stereotypes.
6. Twelve seats mode gives each student a role card.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.
