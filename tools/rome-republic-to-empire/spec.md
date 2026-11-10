# Rome: Republic to Empire

## One idea
The child plays one senator's family across five real turning points from 133 BCE to 27 BCE (Tiberius Gracchus's land law, Marius's army of paid volunteers, Sulla's march on Rome, Caesar crossing the Rubicon, Augustus's settlement), and at each the family chooses (back the reform, side with a general, stay silent, leave Rome); the family's fate branches, but history doesn't, and a government chart beside the story keeps its offices (two consuls, the Senate, the assemblies, the tribunes) standing while power meters drain from them toward generals and finally one man, so a sixth grader sees how a republic can turn into an empire without its offices disappearing, sorts what changed and what continued, maps the causes, and compares how the U.S. Constitution spreads power.

## Not like
- agora-assembly (6, spec): one vote in Athens and Sparta. Here a century of change in Rome's government.
- constantinople-defense (concept): the eastern empire much later. Here the end of the Republic.
- two-parties (concept): early U.S. politics. Here Rome, with a U.S. compare card at the end.
- settle-the-valley (4, spec): a place changing over decades. Here a government changing over a century.

## Who and how
- Grade 6, Social Studies (World History and Civics), module "Ancient Rome". Standards: D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.Civ.5.6-8 (explain the origins, functions, and structure of government with reference to the U.S. Constitution, state constitutions, and selected other systems of government), D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past).
- Format: story. Driver: one child alone, or the class voting on the family's choices (tool.json `driver: "either"`). `Read` reads every page. Controls 44 px or more.
- Five turning points, then the sort, the cause web and the U.S. compare card. Extra: Class vote (each choice shown for a class vote before the teacher taps). tool.json `modes: ["Story", "Class vote"]`, `minutes: "30-40"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.5.6-8 | Tap each office on the government chart to read its job, and watch the power meters move after each turning point; at the end match each Roman safeguard to its U.S. counterpart | the chart with meters; the U.S. compare card | 2, 5 |
| D2.His.2.6-8 | Sort ten developments into Changed, Continued or Both | the sort board under Augustus | 3 |
| D2.His.14.6-8 | Link causes to the Republic's fall from the story's turning points | the cause web with four causes and their effects | 4 |

## Screens and modes
Header (kit): title "Rome: Republic to Empire"; `Story`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Senate house in Rome, 133 BCE. Beside it, the government chart: two consuls (elected each year), the Senate (former officials, for life), the assemblies (citizens vote on laws and elect officials), ten tribunes (protect ordinary citizens and can block laws). Each has a power meter. The family, the Sentii (made up), stand at the door: the senator Quintus, his wife Aemilia, their son Gaius. The welcome is queued (`welcomeAfter: true`): "Rome is a republic. No one person rules. Your family has a seat in the Senate. Over the next hundred years, five moments will test it. Tap the first moment." First hint: "Tap 133 BCE."

**The story (focus: one turning point at a time, with the chart).** At 1366x768 the story page sits left and the chart right; at 680x425 the chart is a tab with a small meter strip always showing.
1. 133 BCE, Tiberius Gracchus's land law. Small farmers who fought in Rome's wars came home to find rich families' huge estates, worked by enslaved people, had swallowed their land. Tiberius, a tribune, passes a law to give public land to poor citizens, going around the Senate. When he runs for tribune again, senators and their supporters beat him and about 300 followers to death. Choice: back the land law; oppose it; stay silent. Chart: the Senate's meter dips (violence enters politics), the tribunes' rises then falls.
2. 107 BCE, Marius's army. Marius, elected consul, takes landless volunteers into the army with pay and the promise of land after service; soldiers look to their general, not the Senate, for their future. Choice: Gaius joins Marius's legion; Gaius stays home; the family funds a rival. Chart: a new meter appears, "Generals", and starts to rise.
3. 88 BCE, Sulla marches on Rome. For the first time a Roman general leads his army into the city; later, as dictator (82 to 79 BCE), he posts lists of enemies who may be killed and their property taken. Choice: side with Sulla; side with Marius's party; leave Rome for the family's farm. The family's fate branches (gains office, loses land on the lists, or waits it out). Chart: Generals rise sharply.
4. 49 BCE, Caesar crosses the Rubicon. Ordered to give up his army, Julius Caesar crosses the river into Italy with it, starting a civil war; in 44 BCE he is named dictator for life and is killed in the Senate house on March 15 by senators who say they are saving the Republic. Choice: side with Caesar; side with Pompey and the Senate; stay neutral. Chart: "Generals" becomes "One man" and fills; the Senate and assemblies drain.
5. 27 BCE, Augustus's settlement. After more civil war and his win at Actium (31 BCE), Octavian says he is giving power back to the Senate and people; the Senate names him Augustus. He keeps command of the provinces with the most legions, and the offices go on. Choice: take an office Augustus offers; retire to the farm. Chart: every office label is still there; "One man" holds nearly all the power. The narrator: "The offices kept their names. The power had moved."
- Each choice changes only the Sentii's own story (who lives where, who holds what office), never the history around them; the page says so: "You can change your family's story. You can't change Rome's."

**What changed, what continued (D2.His.2.6-8).** Ten cards to sort: consuls still elected each year (Both: still elected, but Augustus picks who wins); the Senate still meets (Continued, with less power); one man commands the armies (Changed); peace inside Rome after a century of civil wars (Changed); Latin, roads and Roman law (Continued); tribunes' power (Changed: Augustus holds tribune power himself); the assemblies still meet (Both, less often and with less power); the provinces and conquests (Continued, growing); violence in politics ends for a time (Changed); the word "Republic" still used (Continued, in name). Each needs a reason tile.

**The cause web (D2.His.14.6-8).** Four cause cards (Land: small farmers lost land to big estates; Armies loyal to generals; Violence in politics; Wealth from conquest) and five effects (the turning points). The child draws links; each cause links to at least one effect, and some effects have more than one cause. Narrator: "The Republic didn't fall for one reason. Each cause made the next one easier."

**The U.S. compare card (D2.Civ.5.6-8).** Roman weaknesses on the left, U.S. safeguards on the right; the child matches them: armies loyal to generals and the military answering to an elected president and Congress (Congress funds the army, the president commands); a dictator for life and a two-term limit on the president (22nd Amendment, 1951); power gathered in one man and three separate branches that check each other; violence to stop a law and courts and elections to change a law. Narrator: "The people who wrote the U.S. Constitution had read Rome's story."

**The end.** The family's path, the final chart, the sort board, the web and the compare card. `Print` prints all four.

## Content
- Five turning-point pages (about 120 words each), three choices each with family outcomes (15 short branch pages), the chart with four meters and their values at each point, ten sort cards, four causes and five effects, four compare pairs.
- The Sentii family and their branch pages are made up and labeled; every event, date, person and office is real.
- The power meters are a teaching model, not a measurement; the chart says "a picture of who had the most say".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Turning points open in order; the family's past choices show as a path at the top.
- Tapping an office on the chart reads its job at that time.
- Keyboard: Tab through choices, chart offices and cards; Enter to choose; arrows in the sort and the web.
- With Motion off meters jump to their value and pages swap without sliding.

## Look
- Accent `--brand` #8a1c1c Roman crimson (header, chart frame, turning-point dates); gold #f4c542 (the current turning point, the chosen card); paper #fbf3ef; ink #2b0a08; muted #63504c.
- Contrast (WCAG 2.1, computed): white on brand 9.28:1; brand on paper 8.47:1; ink on paper 16.67:1; muted on paper 6.89:1; ink on gold 11.23:1.
- Never color alone: meters carry numbers and labels; the sort columns carry words and icons.
- Different from this batch (agora blue, silk road mulberry, border olive, farmer ochre).

## Art
- Public domain: Marble portrait of the emperor Augustus, The Met, accession 07.286.115 (Open Access, object 247993); a portrait coin of Julius Caesar, 44 BCE, from an open-access museum collection, picked and checked at build. Each with credit.
- People art goes to Gemini with `people: true`: the Sentii family (Quintus, Aemilia, Gaius; 3 poses across the century; cutout yes); Tiberius Gracchus addressing citizens; Marius's volunteers; Sulla's army at the city gate; Caesar at the Rubicon (5 scenes).
- Local FLUX (`scripts/localart.py`): the Senate house and Forum (1, 16:9); the family's farm (1, 16:9).
- Drawn in code: the government chart and meters, the sort board, the cause web, the compare card.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator; `wise-mentor` as Quintus Sentius speaking the family's choices aloud. `Curio.voice` with `scope: () => state.mode + ':' + state.point + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each turning-point page.
- how `choose`: "Pick what the Sentii family does."
- event, whole, each branch page.
- how `chart`: "Tap an office on the chart to see its job now."
- how `sort`: "Drag each card to Changed, Continued or Both."
- how `web`: "Tap a cause, then an event it helped cause."
- how `compare`: "Match each Roman weakness to a U.S. safeguard."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the branching story with a fixed history track, the chart with meters, the sort, the cause web and the compare match.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Story | Pick the first choice every time | Any path reaches 27 BCE; the history and chart are the same, which is the point the page names. |
| Sort | Put everything in Changed | "The Senate still meets" in Changed plays "Did the Senate stop meeting? Look at the chart." |
| Cause web | Link every cause to 27 BCE only | Each cause needs a link to the turning point where it first shows; the hint names the year. |
| Compare | Match at random | Each pair checks and explains. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Turning-point page (whole), waits.
2. `choose`; branch page (whole); `chart`.
3. After five: `sort`, `web`, `compare`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.6-8, D2.Civ.5.6-8 and D2.His.14.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Tiberius Gracchus's land law and killing, 133 BCE, with about 300 followers | Plutarch, Life of Tiberius Gracchus 19 to 20 | Encyclopaedia Britannica, "Tiberius Gracchus" | yes |
| Marius enlisted landless volunteers as consul in 107 BCE | Sallust, The Jugurthine War 86 | Encyclopaedia Britannica, "Gaius Marius" | yes |
| Sulla marched on Rome in 88 BCE; dictator 82 to 79 BCE; proscriptions | Plutarch, Life of Sulla 9 and 31 | Encyclopaedia Britannica, "Lucius Cornelius Sulla" | yes |
| Caesar crossed the Rubicon in January 49 BCE; named dictator for life and killed March 15, 44 BCE | Suetonius, Life of Julius Caesar 31 to 32 and 76 to 82 | Encyclopaedia Britannica, "Julius Caesar" | yes |
| Actium, 31 BCE; Octavian named Augustus in January 27 BCE while keeping the provinces with most legions | Augustus, Res Gestae 34 | Met Heilbrunn Timeline, "Augustan Rome" | yes |
| The Republic's offices: two consuls, the Senate, assemblies, ten tribunes | Encyclopaedia Britannica, "Roman Republic" | Met Heilbrunn Timeline, "The Roman Republic" | yes |
| U.S. safeguards: Congress funds the army and the president commands it; 22nd Amendment (1951); three branches | National Archives, Constitution transcript, Article I section 8 and Article II section 2 | National Archives, 22nd Amendment | yes |
| Marble portrait of Augustus, The Met 07.286.115, Open Access | The Met, object 247993 | The Met, Heilbrunn Timeline entry for the same object | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-09): the five turning points sort as 133, 107, 88, 49, 27 BCE and span 106 years; each of the four causes links to at least one turning point and each turning point has a cause; each family path reaches 27 BCE; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 story and chart side by side; at 680x425 the chart is a tab with a meter strip.
2. The chart keeps every office while its meters move after each turning point. (D2.Civ.5.6-8)
3. The sort checks ten cards with reasons. (D2.His.2.6-8)
4. The cause web takes links from causes to turning points. (D2.His.14.6-8)
5. The U.S. compare card matches four pairs. (D2.Civ.5.6-8)
6. Family choices change only the family's pages.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding or animated meters; no network requests.

## Open questions
None.
