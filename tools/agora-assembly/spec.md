# Agora Assembly

## One idea
The child is an Athenian citizen on the Pnyx hill in 483 BCE, when a rich new vein of silver has been struck at the Laurion mines and the assembly must decide a real question: share the silver out, ten drachmas to each citizen, or build a fleet of warships as Themistocles urges; they hear speakers, pick arguments to answer, and vote by show of hands, then carry the same question to Sparta, where elders and ephors set the question, the assembly shouts, and the elders can set a "crooked" answer aside, while a side bench holds the people who never got a say (an Athenian woman, a metic merchant, an enslaved miner who dug the silver), so a sixth grader compares how two Greek cities decided, and asks why Athens' assembly is remembered as important and what that memory leaves out.

## Not like
- motion-on-the-floor (concept): modern meeting rules. Here two ancient ways of deciding.
- rome-republic-to-empire (6, spec): one senator's family over a century. Here one decision in two cities.
- constitutional-convention (8, concept): negotiating a written plan. Here a single vote and who could cast it.
- town-council (2, spec): a modern council. Here citizens deciding directly.

## Who and how
- Grade 6, Social Studies (World History), module "Ancient Greece". Standards: D2.His.3.6-8 (use questions generated about individuals and groups to analyze why they, and the developments they shaped, are seen as historically significant), D2.Civ.9.6-8 (compare deliberative processes used by a wide variety of groups in various settings).
- Change from the module codes: D2.Civ.8.6-8 (democratic principles in the founding documents of the United States) moves to constitutional-convention, as the idea card proposes; Athens can't teach the U.S. founding documents well (see Open questions).
- Format: roleplay. Driver: one child alone, or the class as the assembly (tool.json `driver: "either"`). `Read` reads every speech. Controls 44 px or more.
- Three parts: Athens, Sparta, the side bench and the compare board. Extra: Class assembly (the class votes by real show of hands; the teacher enters the count). tool.json `modes: ["Assembly", "Class assembly"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.9.6-8 | Decide the same question in Athens and in Sparta, then fill the compare board | the two processes step by step; the compare board's six rows | 2, 3, 4 |
| D2.His.3.6-8 | Pick questions to ask Themistocles and each person on the side bench, then write why the assembly is seen as significant and what that leaves out | question tiles and answers; the two-part significance card | 5 |

## Screens and modes
Header (kit): title "Agora Assembly"; `Assembly`, `Class assembly`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Pnyx hill at dawn: rows of men sitting on the slope, a stone speaker's platform, the city below. The child holds a citizen's token. To one side, a low bench behind a rope with three figures. The welcome is queued (`welcomeAfter: true`): "It's 483 BCE. Miners have struck new silver at Laurion. Today the citizens of Athens decide what to do with it. Tap the herald to open the assembly." First hint: "Tap the herald."

**Athens (focus: the platform and the token).** At 1366x768 the hill fills the screen with the platform center and the side bench at the left edge; at 680x425 the bench becomes a tab.
1. The herald asks, "Who wishes to speak?" (any citizen may).
2. Speakers (each a tap): Demaratos, a farmer (made for this game): "The silver is ours. Ten drachmas each. My family needs it." Themistocles (real): "Aegina's ships raid our coast, and Persia may come again. Build ships." A potter, Lysis (made for this game): "Ships need rowers. Rowers are poor citizens like me. Ships mean pay for us."
3. Answer an argument: the child picks one argument to answer and one tile to answer with (e.g. to the farmer, "Ten drachmas is spent in a month; a fleet protects the farm for years").
4. Vote: show of hands. In Assembly mode the crowd votes with a modeled split leaning to ships; the child's hand counts. In history, the Athenians chose the ships (about 100 to 200 triremes by the ancient accounts), and in 480 BCE that fleet fought at Salamis.

**Sparta (the same question, the Spartan way).** A "what if" card says plainly: Sparta had no silver mines; this asks how Sparta's system would have handled the same choice.
1. The council of elders (the gerousia: 28 men over sixty plus the two kings) talks first and decides what question goes to the assembly.
2. The five ephors, chosen each year, run the meeting.
3. The assembly (Spartan citizen men over thirty) can't debate; they shout yes or no, and the louder shout wins. The child taps and holds to "shout"; a loudness meter fills.
4. If the elders think the people "spoke crookedly", they can set the answer aside. The child sees the elders' choice to accept or set aside.

**The side bench (focus: three people who could not vote).** The child picks questions from tiles to ask each (e.g. "Who decided for you?", "What would the silver mean for you?", "Could you ever vote?").
- Thalia, an Athenian citizen's wife (made for this game): women couldn't attend or vote; her husband decides.
- Kephalos, a metic (a free foreigner living in Athens, made for this game): pays the metic tax and serves in the army, but can't vote or own land.
- Manes, an enslaved miner at Laurion (made for this game): the silver came from mines worked mostly by enslaved people; he dug it and will see none of it.
- Then a numbers card: in the 400s BCE, adult male citizens were a small share of Athens' people; estimates put citizens at around 30,000 out of a total of perhaps 250,000 or more.

**The compare board (the aha).** Two columns, Athens and Sparta, six rows the child fills from tiles: Who could vote? Who set the question? Who could speak? How were votes counted? Could the result be overturned? Who was left out? Then the significance card: "Why is Athens' assembly remembered as important?" (tiles plus a free line: ordinary citizens decided directly; any citizen could speak; the vote built the fleet that won at Salamis) and "What does that memory leave out?" (the side bench). `Print` prints the board and the card.

**Class assembly (extra).** The class votes by real show of hands; the teacher enters the yes and no counts; Sparta's round uses a real class shout.

## Content
- Three Athenian speakers, two answer sets, the Spartan four steps, three side-bench people with three question tiles each, the numbers card, the compare board, the significance card.
- Themistocles, the Laurion silver, the vote, Salamis, the Spartan offices and the shout vote are real; Demaratos, Lysis, Thalia, Kephalos and Manes are made up and labeled.
- The two ancient accounts differ on the fleet size (Herodotus says 200 ships; the Athenian Constitution says 100); the tool says "about 100 to 200, the ancient writers disagree".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The Spartan shout is a press-and-hold (or Space held down) that fills the loudness meter; with Sound off the meter still fills.
- Compare board rows fill by tapping a tile, then a cell.
- Keyboard: Tab through speakers, tiles and cells; Enter to choose; Space held to shout.
- With Motion off the crowd doesn't wave hands and the meter jumps.

## Look
- Accent `--brand` #2b5d8a Aegean blue (header, the platform, Athens column); gold #f4c542 (the citizen's token, the chosen tile); paper #f1f5f9; ink #0c1a26; muted #4d5761.
- Contrast (WCAG 2.1, computed): white on brand 6.92:1; brand on paper 6.32:1; ink on paper 16.09:1; muted on paper 6.72:1; ink on gold 10.84:1.
- Never color alone: the Athens and Sparta columns carry their names and icons (an owl, a shield); left-out rows carry the word "No".
- Different from this batch (silk road mulberry, Rome crimson, border olive, farmer ochre).

## Art
- People art goes to Gemini with `people: true`: Themistocles (from the Roman copy of his portrait at Ostia, for likeness), Demaratos, Lysis, the herald, Thalia, Kephalos, Manes, the Spartan elders and ephors (1 each; cutout yes).
- Public domain (Met Open Access, checked at build for the open-access flag): an Athenian silver tetradrachm with the owl, about 480s to 450s BCE; a red-figure vase with a trireme or rowers if one is open access, otherwise a drawn trireme.
- Local FLUX (`scripts/localart.py`): the Pnyx at dawn (1, 16:9); the Spartan assembly ground (1, 16:9).
- Drawn in code: the token, the loudness meter, the compare board.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator, herald and side-bench reader; `firm-captain` as Themistocles. `Curio.voice` with `scope: () => state.mode + ':' + state.city + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each speech.
- how `answer`: "Pick an argument to answer, then your answer."
- how `vote`: "Raise your hand: tap Ships or Share."
- event, whole, the vote result and history.
- how `shout`: "Press and hold to shout yes or no."
- event, whole, the elders' choice.
- how `ask`: "Pick a question to ask."
- event, whole, each side-bench answer.
- how `board`: "Fill each row of the compare board."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the speaker sequence, the hand vote with a modeled crowd, the shout meter, the side-bench questions, the compare board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Compare board | Fill both columns the same | Each cell checks its tile; a wrong one plays "Who set the question in Sparta? Look back at the elders." |
| Side bench | Skip it | The compare board's "Who was left out?" row and the significance card wait until each person has been asked one question. |
| Significance | Write only praise | The card has two required parts; the second asks what the memory leaves out. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Speeches (whole), each waits.
2. `answer`; `vote`; result (whole).
3. Sparta steps (whole); `shout`; elders' choice (whole).
4. `ask`; answers (whole). `board`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.3.6-8 and D2.Civ.9.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Laurion silver strike, 483 BCE; the choice between sharing ten drachmas each and building ships; Themistocles' proposal | Herodotus, Histories 7.144 | Aristotle (school of), Athenian Constitution 22.7 | yes on the choice; they differ on 100 or 200 ships, shown as a range |
| The fleet fought at Salamis, 480 BCE | Herodotus, Histories book 8 | Encyclopaedia Britannica, "Battle of Salamis" | yes |
| The Athenian assembly met on the Pnyx; any citizen could speak; votes by show of hands | Encyclopaedia Britannica, "Ecclesia" | Stoa Consortium / Dēmos (Neel Smith and Christopher Blackwell), "The Athenian assembly" | yes |
| Women, metics and enslaved people could not vote; rough citizen and population figures | Encyclopaedia Britannica, "Metic" and "Athenian democracy" | Dēmos (Blackwell), "Athenian democracy: a brief overview" | yes, figures given as estimates |
| The Laurion mines were worked mostly by enslaved people | Encyclopaedia Britannica, "Laurium" | Xenophon, Ways and Means (Poroi) 4 | yes |
| Sparta's gerousia (28 elders over sixty plus two kings), five ephors, assembly of men over thirty voting by shout; elders could set aside a "crooked" decision | Plutarch, Life of Lycurgus 6 and 26 | Thucydides 1.87 (vote by shout); Encyclopaedia Britannica, "Gerousia" and "Ephor" | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-09): 28 elders plus 2 kings is 30 in the gerousia; 483 BCE comes three years before 480 BCE; the compare board has 12 cells and each has one right tile; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 hill, platform and bench; at 680x425 the bench is a tab.
2. Athens runs speakers, an answer, and the hand vote with the history line. (D2.Civ.9.6-8)
3. Sparta runs elders, ephors, the shout and the elders' choice, labeled "what if". (D2.Civ.9.6-8)
4. The compare board fills and checks each cell. (D2.Civ.9.6-8)
5. Each side-bench person answers a question; the significance card takes both parts. (D2.His.3.6-8)
6. Class assembly accepts real counts.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no waving crowd; no network requests.

## Open questions
- The module lists D2.Civ.8.6-8 (principles in the U.S. founding documents), which Athens can't teach well (default used: it moves to constitutional-convention; module code list left for Cory).
