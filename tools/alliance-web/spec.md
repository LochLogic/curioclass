# Alliance Web

## One idea
Europe in 1914 appears as a web: the great powers and Serbia and Belgium as nodes, threads for alliances, rivalries, empires and war plans, and a spark in Sarajevo; the student runs the July Crisis day by day (the assassination on June 28, Germany's promise of support, Austria-Hungary's ultimatum on July 23, the declaration of war on Serbia, Russia's mobilization, Germany's declarations, the march through Belgium, Britain's entry on August 4), and each step lights the thread that carried it, with a real telegram, treaty or war plan as evidence; then the student rewinds, changes one long-term cause (no naval race, a war plan that allowed delay, a calmer Balkans, no blank promise from Berlin) and replays, and each outcome is labeled as one side of a historians' debate, not a fact; at the end the student sorts causes into long-term (militarism, alliances, imperialism, nationalism) and triggering (the assassination, the ultimatum, mobilization) and writes a short argument about which mattered most, then a last step shows what the peace of 1919 changed and what it set up next, so a ninth grader learns to analyze many interacting causes and effects and to tell long-term causes from triggers in a historical argument.

## Not like
- claim-repair-shop (10, concept): repairs broken explanations. Here the causes of one war.
- ideas-that-spread (9, spec): ideas on a map. Here threads in a web.
- civil-war-map-room (8, spec): ranking causes of a victory. Here long-term causes against triggers.
- constantinople-defense (7, spec): many causes of one fall. Here a chain reaction across a continent.

## Who and how
- Grade 9, Social Studies (World History), module "World War I". Standards: D2.His.14.9-12 (analyze multiple and complex causes and effects of events in the past), D2.His.15.9-12 (distinguish between long-term causes and triggering events in developing a historical argument).
- Format: simulator. Driver: one student alone, or class teams (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- The July Crisis in twelve steps, four what-if replays, the sort, the argument, the 1919 step. Extra: Team claims (teams each defend a different "most important cause" with evidence from the web, then the class votes). tool.json `modes: ["The web", "Team claims"]`, `minutes: "30-40"`, `grades_label: "Grade 9"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.14.9-12 | Step through the July Crisis, then change one long-term cause and replay | threads lighting with evidence; the replay with its debate label | 2, 3 |
| D2.His.15.9-12 | Sort causes into long-term and triggering, then write an argument naming the most important | the sort board; the argument card | 4, 5 |

## Screens and modes
Header (kit): title "Alliance Web"; `The web`, `Team claims`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A dark map of Europe in 1914 with nodes for Germany, Austria-Hungary, Italy, France, Russia, Britain, Serbia, Belgium and the Ottoman Empire, threads labeled by kind (alliance, rivalry, empire, war plan), and a small spark at Sarajevo. The welcome is queued (`welcomeAfter: true`): "On June 28, 1914, two shots in Sarajevo killed the heir to Austria-Hungary's throne. Five weeks later most of Europe was at war. How? Tap the spark." First hint: "Tap the spark."

**The July Crisis (focus: the web and the day card).** At 1366x768 the web fills the left with the day card right; at 680x425 the card is a sheet. Twelve steps, each lighting its thread and showing evidence (under 15 words quoted, credited):
1. June 28: Gavrilo Princip, a Bosnian Serb member of Young Bosnia armed with help from Serbian officers in the Black Hand, kills Archduke Franz Ferdinand and his wife Sophie.
2. July 5 to 6: Germany promises Austria-Hungary full support (the "blank cheque").
3. July 23: Austria-Hungary's ultimatum to Serbia, with 48 hours to answer.
4. July 25: Serbia accepts most terms but not all; Austria-Hungary breaks relations.
5. July 28: Austria-Hungary declares war on Serbia.
6. July 29 to August 1: the "Willy-Nicky" telegrams between Kaiser Wilhelm II and Tsar Nicholas II.
7. July 30: Russia orders general mobilization.
8. August 1: Germany declares war on Russia; France mobilizes.
9. August 3: Germany declares war on France; its war plan (the Schlieffen Plan) requires going through Belgium.
10. August 4: German troops enter Belgium, whose neutrality Britain had guaranteed in the Treaty of London (1839); the German chancellor calls the treaty a "scrap of paper".
11. August 4: Britain declares war on Germany.
12. Later in 1914: the Ottoman Empire joins Germany; Italy stays out until 1915 and then joins the other side.
- Long-term threads carry their own evidence cards: the alliance system (the Triple Alliance, 1882; the Franco-Russian alliance, 1894; the Entente Cordiale, 1904; the Anglo-Russian entente, 1907); the naval race (HMS Dreadnought, 1906); rivalry over empire (the Moroccan crises of 1905 and 1911); nationalism in the Balkans (Austria-Hungary's annexation of Bosnia, 1908; the Balkan Wars, 1912 to 1913); war plans with fixed timetables.

**What-if replays (D2.His.14.9-12).** The student rewinds and changes one long-term cause from four: no naval race; a German war plan that could fight Russia alone; no blank cheque; a calmer Balkans. The web replays; some threads stay dark. Each outcome is labeled with the historians who would argue it (for example Fritz Fischer, who stressed German aims; Christopher Clark, who described leaders on all sides as "sleepwalkers"; Margaret MacMillan, who stressed choices that could have gone the other way), and with a note: "This is one side of a debate, not what would have happened."

**The sort and the argument (the aha, D2.His.15.9-12).** Cards to sort into long-term causes (militarism, alliances, imperialism, nationalism, war plans) and triggering events (the assassination, the blank cheque, the ultimatum, mobilization, the invasion of Belgium). Then the argument card: "The most important cause of the war was ___ because ___. The trigger mattered because ___. Without ___, I think ___." Narrator: "A spark needs fuel. Historians still argue about which fuel mattered most."

**1919.** A last step: the Treaty of Versailles (signed June 28, 1919, five years to the day after Sarajevo), its war-guilt clause (Article 231), the League of Nations, four empires gone (German, Austro-Hungarian, Russian, Ottoman), new states drawn in Europe and new mandates in the Middle East; about 9 to 10 million soldiers dead, given as a number with no images of the dead. The student links one effect to what it set up next.

**The end.** The web with the student's lit threads, the replays, the sort and the argument. `Print` prints them.

**Team claims (extra).** Teams defend different "most important cause" claims with evidence cards from the web; the class votes.

## Content
- Nine nodes, about twenty threads with evidence cards, twelve crisis steps, four what-if replays with historians' labels, ten sort cards, the argument card, the 1919 step.
- All people, dates, documents and figures are real and sourced; replay outcomes are labeled as historians' arguments, never facts.
- Leaders are shown in public domain photographs.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Crisis steps go in order; the student can step back.
- A replay changes one cause at a time; changing another resets the first.
- Keyboard: Tab to nodes, threads, steps, what-if switches, cards and the argument; arrows step the crisis; Enter to open and place.
- With Motion off threads light at once without pulsing.

## Look
- Accent `--brand` #4f5a2a field olive (header, the web frame, cards); gold #f4c542 (the lit thread, a sorted card); paper #f5f6ef; ink #171a0b; muted #575a4c.
- Contrast (WCAG 2.1, computed): white on brand 7.42:1; brand on paper 6.83:1; ink on paper 16.24:1; muted on paper 6.50:1; ink on gold 10.86:1.
- Never color alone: thread kinds carry labels and dash patterns (solid alliance, dashed rivalry, dotted war plan, double empire); lit threads thicken.
- Different from this batch (ochre, mill soot, cartographer blue, Atlantic indigo).

## Art
- Public domain (Library of Congress, Imperial War Museums non-commercial public domain items, ids checked at build): photographs of Franz Ferdinand and Sophie (1914), Wilhelm II, Nicholas II, George V, Raymond Poincare; HMS Dreadnought (1906); the Treaty of London (1839) page; the Versailles signing painting by Orpen (1919) if public domain where used, otherwise a Library of Congress photograph. Each with credit.
- Local FLUX (`scripts/localart.py`): a period-style map of Europe as the web's base (1, 16:9).
- Drawn in code: nodes, threads, cards, the sort board.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the day-by-day crisis announcer; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each crisis step.
- event, whole, each evidence card.
- how `step`: "Tap Next day to see which thread carries the crisis."
- how `whatif`: "Change one long-term cause, then tap Replay."
- event, whole, each replay's debate label.
- how `sort`: "Sort each card into long-term or trigger."
- how `argue`: "Write your argument about the most important cause."
- event, whole, the 1919 step.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the node and thread web, the crisis stepper, the replay model with debate labels, the sort board, the argument card, the 1919 step.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Replays | Skip them | The sort opens after two replays. |
| Sort | Call everything long-term | Each card checks; the assassination as long-term plays a reason line. |
| Argument | Name a cause with no evidence | The argument must cite one evidence card from the web; Print waits. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `step`; crisis step (whole), waits; evidence card (whole).
2. `whatif`; replay debate label (whole).
3. `sort`; `argue`.
4. The 1919 step (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.9-12 and D2.His.15.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The assassination (June 28, 1914), Princip, Young Bosnia and the Black Hand | Clark, "The Sleepwalkers" (Allen Lane, 2012) | Britannica, "Assassination of Archduke Franz Ferdinand" | yes |
| The blank cheque, the ultimatum (July 23), war on Serbia (July 28), Russian mobilization (July 30), declarations (August 1, 3), Belgium and Britain (August 4) | Imperial War Museums, "The July Crisis" timeline | MacMillan, "The War That Ended Peace" (Random House, 2013) | yes |
| The Willy-Nicky telegrams | Brigham Young University, World War I Document Archive | Clark (2012) | yes |
| The Treaty of London (1839) and the "scrap of paper" | UK National Archives, "Treaty of London 1839" | Britannica, "Scrap of paper" | yes |
| Alliances: 1882, 1894, 1904, 1907; Dreadnought 1906; Moroccan crises 1905, 1911; Bosnia 1908; Balkan Wars 1912-13 | Britannica entries for each | MacMillan (2013) | yes |
| Historians' debate: Fischer on German aims; Clark's "sleepwalkers"; MacMillan on choices | Fischer, "Germany's Aims in the First World War" (1961; English 1967) | Clark (2012); MacMillan (2013) | yes |
| Versailles signed June 28, 1919; Article 231; about 9 to 10 million soldiers dead | U.S. Department of State, Office of the Historian, "Paris Peace Conference" | Imperial War Museums, "First World War casualties" | yes, as a range |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r17, 2026-11-09): crisis dates in order (June 28; July 5, 23, 25, 28, 29, 30; August 1, 3, 4); 37 days from June 28 to August 4 is just over five weeks; Versailles signed exactly five years after Sarajevo; five long-term and five trigger cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 web and day card; at 680x425 sheet.
2. Twelve crisis steps light their threads with evidence. (D2.His.14.9-12)
3. Four what-if replays run, each labeled as a historians' argument. (D2.His.14.9-12)
4. The sort checks long-term causes against triggers. (D2.His.15.9-12)
5. The argument cites evidence and prints. (D2.His.15.9-12)
6. The 1919 step links one effect to what it set up.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: threads light without pulsing; no network requests.

## Open questions
- The idea card flags overlap with claim-repair-shop, whose card also touches World War I causes (default used: World War I causes live here, and claim-repair-shop takes a different topic as its card proposes).
