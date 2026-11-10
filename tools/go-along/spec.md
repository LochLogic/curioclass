# Go Along?

## One idea
A start card says "this activity has a surprise, and it will be explained right after"; then the student sits at a classroom table with five illustrated classmates and a card of lines, "Which line matches?", and on some rounds every classmate gives the same wrong answer before the student's turn; right after the run the tool reveals that the classmates were scripted, shows the student's own answers beside Solomon Asch's results (about a third of answers on the critical trials went along, three in four people went along at least once), then lets the student change the conditions (one ally who answers right, a private written answer, a group of two, four or eight) and see how conformity shifts in the published findings; two more rooms present documented history, not re-enactments: the bystander studies (Darley and Latané's 1968 seizure study, and what the famous 1964 Kitty Genovese story got wrong, including the neighbor who went to her) and Milgram's obedience studies (26 of 40 went to the highest shock in the 1963 study, and what later reanalysis and a 2009 partial replication found); for each study the student rates harm, consent and deception against today's research rules and sees why the rules changed; at the end the student writes a "when I'd speak up" note that stays on the device, and reads the evidence that in real public conflicts someone usually steps in, so a twelfth grader learns conformity, obedience and the bystander effect, the conditions that change them, and research ethics.

## Not like
- illusion-lab (12, spec): perception. Here social pressure.
- jury-room (12, spec): deliberating to a verdict. Here the pull to agree.
- brain-explorer (12, spec): biology. Here the social situation.
- trait-lab (12, spec): individual differences. Here the power of the group.

## Who and how
- Grade 12, Psychology, module "Social Psychology". Standards: APA.Sociocultural (APA National Standards for High School Psychology Curricula: social influence, including conformity, obedience and the bystander effect, and the ethics of research with people). APA.Individual Variations is taught in trait-lab and APA.Mental and Physical Health in case-conference, as the idea card proposes.
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- The line task (18 rounds, 12 critical), four changed conditions, two history rooms, the ethics ratings, the note. Extra: Class run (an anonymous class line task on one screen, counting only how many went along). tool.json `modes: ["Lab", "Class run"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Sociocultural (conformity) | Answer the line task, then change ally, privacy and group size | the student's answers beside Asch's; the condition chart | 2 |
| APA.Sociocultural (bystander) | Step through the seizure study and the Genovese record | the helping rates by group size; the corrected story | 3 |
| APA.Sociocultural (obedience) | Step through Milgram's study and the later findings | the shock board; the variations chart | 4 |
| APA.Sociocultural (ethics) | Rate harm, consent and deception for each study | the ethics card against today's rules | 5 |

## Screens and modes
Header (kit): title "Go Along?"; `Lab`, `Class run`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A start card: "This activity has a surprise. It will be explained right after, and you can skip it any time." Then a classroom table with five illustrated classmates (made up) and a card of four lines. The welcome is queued (`welcomeAfter: true`): "Look at the line on the left. Which line on the right matches it? Everyone answers out loud, and you go last. Tap your answer." First hint: "Tap line A, B or C."

**The line task (focus: the card and the faces).** At 1366x768 the table fills the screen with the card in the middle; at 680x425 the card sits above the faces. Eighteen rounds; on twelve, all five classmates say the same wrong line first. A `Skip` button is always there.
- The reveal: the classmates were scripted; the student's answers sit beside Asch's: about a third of answers on critical trials conformed; about three in four people conformed at least once; about one in four never did.
- Conditions: one ally who answers right (conformity drops sharply); a private written answer (it drops); a group of two, four or eight (it rises to about three or four and then levels off).

**The bystander room.** Darley and Latané (1968): students heard someone have a seizure over an intercom; alone, 85 percent went for help before it ended; with four others believed present, 31 percent. The Genovese record: the 1964 news story said 38 people watched and did nothing; later reporting found far fewer saw the attack, at least one called police, and a neighbor, Sophia Farrar, went to her. Evidence card: in recorded real public conflicts, someone stepped in nine times in ten (Philpot and colleagues, 2019).

**The obedience room.** Milgram (1963): 26 of 40 men continued to the highest level of a fake shock board when an experimenter told them to; variations changed the rate (the experimenter by phone, a peer who refused). Later findings: many participants doubted the set-up, and a 2009 partial replication stopped at 150 volts for ethics (Burger). Presented with photos of the board only, no recreated distress.

**Ethics.** For each study the student rates harm, consent and deception against today's rules (informed consent, debriefing, the right to stop, review boards after the National Research Act of 1974 and the Belmont Report of 1979). The student's own surprise is rated too: brief, explained at once, with a right to skip.

**The note (the aha).** "I'd speak up when ___. What makes it easier is ___ (an ally, a private way, knowing someone is counting on me)." It stays on the device and the screen says so. Narrator: "The studies show how strong the pull is. They also show that one person who speaks up changes the room."

**The end.** The condition chart, the two rooms, the ethics ratings and the note (printed only if the student chooses). `Print` prints them.

**Class run (extra).** The class answers on one screen anonymously; only the count who went along is shown.

## Content
- Five made-up classmates, 18 line rounds (12 critical), four conditions with published results, two history rooms with real data, ethics cards, the note.
- No re-enactment of the bystander or obedience studies; no original study photos unless public domain and checked; the line task is skippable.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The reveal comes straight after the last round or after `Skip`.
- The note saves to the device (localStorage `go-along-v1`, try/catch) with a clear button; nothing is sent.
- Keyboard: Tab to answers, conditions, rooms, ratings and the note; A, B and C keys answer.
- With Motion off classmates speak without animating.

## Look
- Accent `--brand` #8c1c3a line crimson (header, the line card, charts); gold #f4c542 (the student's answer, the ally); paper #fbf0f3; ink #2a0711; muted #5f5156.
- Contrast (WCAG 2.1, computed): white on brand 8.97:1; brand on paper 8.05:1; ink on paper 16.59:1; muted on paper 6.74:1; ink on gold 11.36:1.
- Never color alone: lines carry letters; chart bars carry numbers; ratings carry words.
- Different from this batch (harvest ochre, clinic teal, clock blue, map slate).

## Art
- People (illustrated) for five classmates with a speaking pose each, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the classroom table (1, 16:9), an intercom room (1, 16:9), a lab with a shock board and no people (1, 16:9), a 1960s city street at night with no people (1, 16:9).
- Drawn in code: the line cards, charts, ethics cards.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the researcher who reveals and explains; `clear-teacher` as the history rooms, ethics and hints. Five classmates use short recorded lines from the same two voices with pitch kept natural. `Curio.voice` with `scope: () => state.mode + ':' + state.room + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `answer`: "Tap the line that matches."
- event, whole, the reveal.
- how `condition`: "Pick a condition to change."
- event, whole, each history room.
- how `rate`: "Rate harm, consent and deception."
- how `note`: "Write when you'd speak up."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the line task, conditions, history rooms, ethics ratings, the note.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Line task | Skip it | Allowed; the reveal and conditions still teach from Asch's data. |
| Conditions | Try one | The chart needs all four before the rooms open. |
| Ethics | Rate everything "fine" | Each rating shows today's rule it breaks and asks for a reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: start card; `welcome` (queued). `answer`.
2. Reveal (whole), waits; `condition`.
3. History rooms (whole); `rate`.
4. `note`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| APA.Sociocultural wording | APA, "National Standards for High School Psychology Curricula" (2022) | data/modules/social-studies.txt | yes |
| Asch: about a third conformed on critical trials, three in four at least once, an ally cuts it | Asch, Psychological Monographs (1956) | Bond and Smith, Psychological Bulletin (1996) | yes |
| Group size effect levels off near three or four | Asch, Scientific American (1955) | Bond, Group Processes and Intergroup Relations (2005) | yes |
| Seizure study: 85 percent alone, 31 percent with four others | Darley and Latané, Journal of Personality and Social Psychology (1968) | APA, "The bystander effect" | yes |
| The Genovese story's errors; Sophia Farrar | Manning, Levine and Collins, American Psychologist (2007) | The New York Times, "Kitty Genovese, Who Was Killed as Neighbors Looked On" correction note (2016) | yes |
| Milgram: 26 of 40 to the highest level; Burger's 2009 partial replication | Milgram, Journal of Abnormal and Social Psychology (1963) | Burger, American Psychologist (2009) | yes |
| Someone intervenes in most real public conflicts | Philpot and colleagues, American Psychologist (2019) | Levine and colleagues, Personality and Social Psychology Review (2020) | yes |
| National Research Act (1974) and Belmont Report (1979) | HHS Office for Human Research Protections, "The Belmont Report" | National Institutes of Health, history of human subjects protection | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the tool uses a brief, announced, skippable deception and explains it at once; obedience and bystander studies are history with no re-enactment or distress shown; the Genovese murder is described without detail; a fresh agent reads the text before build.

Checks run (Python, scratchpad r24, 2026-11-09): 26 of 40 is 65 percent; 12 critical rounds of 18; the 1964 attack (March 13) came 14 days before the news story (March 27); the Belmont Report came 5 years after the National Research Act; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and card; at 680x425 card above faces.
2. The line task, reveal and four conditions run with Asch's data. (APA.Sociocultural)
3. The bystander room shows the 85 and 31 percent and the corrected Genovese story. (APA.Sociocultural)
4. The obedience room shows Milgram's result and later findings without re-enactment. (APA.Sociocultural)
5. Each study gets harm, consent and deception ratings against today's rules. (APA.Sociocultural)
6. The start card announces the surprise; `Skip` is always there; the note stays on the device.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animation; no network requests.

## Open questions
- Sensitivity flag: research deception and distress in Milgram's study (default used: an announced, skippable surprise explained at once, history rooms with no re-enactment, fresh-agent read before build).
- The idea card moves APA.Individual Variations and APA.Mental and Physical Health out (default used: go-along teaches APA.Sociocultural only; trait-lab and case-conference take the other two).
