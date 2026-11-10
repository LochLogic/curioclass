# Rights Match

## One idea
The child first sits in a 1788 town meeting where a farmer says "No rights written down, no vote from me" and hears how the fight over ratifying the Constitution ended in a promise to add a list of rights, then sorts eight real-life scenario cards (a kids' newsletter, a family going to worship, a march with a permit, a police search of a home, soldiers demanding a bed, a trial without a lawyer, a suspect told to confess, a $10,000 fine for a late library book) into the amendment that protects each, sees the purpose and the principle under every right, and ends weighing two cases where rights meet limits, so a fifth grader learns where the Bill of Rights came from, what it protects and why, and that rights come with duties.

## Not like
- bill-to-law-board-game (4, spec): how a state bill becomes law. Here the rights the Constitution protects and why they were added.
- revolution-road (5, spec): the war years. Here the founding years just after.
- founding-words-explorer (9, concept): reading founding documents closely. Here matching everyday life to rights.
- reconstruction-amendments (8, concept): the 13th to 15th Amendments. Here the first ten.

## Who and how
- Grade 5, Social Studies (Civics), module "The Constitution and Bill of Rights". Standards: D2.Civ.3.3-5 (examine the origins and purposes of rules, laws, and key U.S. constitutional provisions), D2.Civ.4.3-5 (explain how groups of people make rules to create responsibilities and protect freedoms), D2.Civ.8.3-5 (identify core civic virtues and democratic principles that guide government, society, and communities).
- Change from the module codes: D2.Civ.5.3-5 (the structure of state and national government) moves to bill-to-law-board-game, as the idea card proposes; a scenario sort can't teach structure well (see Open questions).
- Format: sort. Driver: one child alone, or the teacher on the projector (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three parts: the 1788 meeting, the sort, and Rights and limits. Extra: Class vote (each scenario shown to the class for a show-of-hands guess before the sort). tool.json `modes: ["Sort", "Class vote"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.3.3-5 | Watch the 1788 meeting and put four ratification steps in order; read each right's purpose after sorting | the step strip (1787 signed, states argue, the promise, 1791 ratified); each right's purpose line | 2, 3 |
| D2.Civ.4.3-5 | Pick what the town meeting decides to do (vote no, vote yes with a list of wanted amendments, walk out) and see what Massachusetts did | the meeting's choices; the Massachusetts vote of 187 to 168 with recommended amendments | 2 |
| D2.Civ.8.3-5 | Sort scenarios into amendments; each correct sort shows the principle and the duty that goes with it | the principle tag and duty line on each card | 3 |
| D2.Civ.8.3-5 (limits) | Weigh two cases where one person's right meets another's | the scales and the child's chosen rule | 4 |

## Screens and modes
Header (kit): title "Rights Match"; `Sort`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A 1788 meeting house. A farmer, Mr. Hale (made for this game), stands with his hat in his hand. Speech bubble: "No rights written down, no vote from me." The welcome is queued (`welcomeAfter: true`): "In 1787 a new Constitution was written. Before it could be used, the states had to say yes. Many people wanted something added first. Tap Mr. Hale to hear why." First hint: "Tap Mr. Hale."

**The 1788 meeting (focus: the meeting house).** Four short scenes, each a tap:
1. Mr. Hale's worry: the Constitution makes a strong national government but doesn't list what it can't do to people (search their homes, stop their newspapers, put soldiers in their houses).
2. A neighbor, Mrs. Avery (made for this game), answers for the Constitution: the states can ask for changes after.
3. Real history: George Mason refused to sign in 1787 because there was no bill of rights; in February 1788 Massachusetts voted 187 to 168 to ratify and sent a list of amendments it wanted.
4. The choice: the child picks what the meeting should do (vote no; vote yes and ask for amendments; walk out). Any choice plays what happened: "Several states did what Massachusetts did. James Madison kept the promise, and in 1791 the first ten amendments, the Bill of Rights, were added."
- Then the child places four steps on a strip: September 1787 the Constitution is signed; 1787 to 1788 the states argue and vote; 1789 Madison writes amendments; December 1791 the Bill of Rights is ratified.

**The sort (focus: the scenario card and six amendment slots).** At 1366x768 the six slots sit in a row below the card; at 680x425 they are a two-by-three grid.
- Slots: 1st (speech, press, religion, gathering, asking the government), 3rd (no soldiers in your home), 4th (no unreasonable searches), 5th (no forcing you to speak against yourself; fair process), 6th (a lawyer and a fair, speedy jury trial), 8th (no cruel punishments or huge fines). Each slot shows its plain words and number.
- Eight scenarios (made for this game, each with a picture):
  1. Maya's neighborhood newsletter says the city should fix the potholes. The mayor wants it stopped. (1st, press; principle: free expression; duty: tell the truth.)
  2. The Haddad family goes to their mosque on Friday; the Lees to church on Sunday; Sam's family to temple on Saturday. (1st, religion; principle: freedom of belief; duty: respect others' beliefs.)
  3. Neighbors hold a march with a city permit to ask for a crosswalk. (1st, gathering and asking; principle: the people can speak to government; duty: keep it peaceful.)
  4. Police want to search a family's house without a warrant from a judge. (4th; principle: privacy and limited government; duty: follow the law so a judge has no reason.)
  5. In 1774, soldiers tell a family to let them sleep in their house. (3rd; this was real before the Revolution; principle: limited government.)
  6. Mr. Diaz goes on trial and asks for a lawyer. (6th; principle: fair treatment and equal justice; duty: serve on a jury when called.)
  7. A suspect is told, "You must say you did it." (5th; principle: fair process.)
  8. A town fines a kid $10,000 for a late library book. (8th, huge fines; principle: fair punishment.)
- Each correct sort turns the card to show the purpose ("Why was this added?"), the principle tag and the duty. A wrong sort: "Read the slot's words again. Which one protects this?" and the card returns.

**Rights and limits (the aha).** Two cases on a balance scale:
1. A march planned across the hospital driveway. One side: the marchers' right to gather. Other side: patients and ambulances. The child picks a rule (ban the march; let it block the driveway; move the march route). Narrator: "The city can't stop the march for what it says, but it can set the time, the place and the route. Rights have limits so other people's rights are safe too."
2. Maya's newsletter prints something false that hurts a neighbor's bakery. The child picks: allowed, because of free press; not allowed, because lies that hurt someone aren't protected. Narrator: "Free press means you can criticize the mayor. It doesn't mean you can tell lies that hurt people."

**The end.** The six slots with their cards, principles and duties. Narrator: "People in 1788 refused to say yes until their freedoms were written down. Each right protects you, and each comes with a duty to others." `Print` prints the slots as a rights chart.

**Class vote (extra).** Each scenario shows to the class with "Which amendment? Show fingers 1, 3, 4, 5, 6 or 8" before the teacher taps to sort.

## Content
- Four meeting scenes, the four-step strip, eight scenarios with purpose, principle and duty, two limits cases, the end chart.
- Mr. Hale, Mrs. Avery, Maya, the Haddads, the Lees, Sam's family and Mr. Diaz are made up and labeled; George Mason, James Madison, the Massachusetts vote and the dates are real.
- Amendment wording shown as the plain version, with the real text a tap away (National Archives transcript).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Drag or tap-then-place sorts a card; the next card appears after a correct sort.
- Keyboard: Tab to the card; Enter to pick it up; arrow keys choose a slot; Enter to drop.
- With Motion off cards turn without flipping and the scale jumps to its tilt.

## Look
- Accent `--brand` #6b2f6b parchment plum (header, slots, principle tags); gold #f4c542 (the picked-up card, the lit step); paper #f8f1f7; ink #250e24; muted #5d5160.
- Contrast (WCAG 2.1, computed): white on brand 9.36:1; brand on paper 8.43:1; ink on paper 16.21:1; muted on paper 6.73:1; ink on gold 11.06:1.
- Never color alone: each slot has its number and an icon (a speech bubble, a house with a soldier crossed out, a house with a key, a closed mouth, a scale, a coin with a cap).
- Different from this batch (scout amber, revolution navy, change teal, Pony Express saddle rust).

## Art
- Public domain, checked at spec: the engrossed Bill of Rights (National Archives, 1789); a portrait of James Madison (Gilbert Stuart, about 1821, National Gallery of Art); a portrait of George Mason (Library of Congress). Each used once with credit.
- People art goes to Gemini with `people: true`: Mr. Hale and Mrs. Avery in the 1788 meeting house (1 scene); eight scenario pictures (Maya with her newsletter, the three families, the march, the police at a door, the 1774 soldiers, Mr. Diaz with a lawyer, the suspect in a room, the kid at the library desk); the two limits cases (2).
- Drawn in code: the slots and icons, the scale, the step strip, the rights chart.
About 14 images.

## Voice
Three bank voices, each unique in this batch: `warm-teacher` as the narrator; `friendly-dad` as Mr. Hale; `lively-host` as Mrs. Avery. `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each meeting scene.
- how `choose`: "Pick what the meeting should do."
- how `strip`: "Put the four steps in order."
- how `sort`: "Drag the card to the amendment that protects it."
- event, whole, each card's purpose and principle.
- how `weigh`: "Pick the fairest rule for both sides."
- event, whole, each limits answer.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
founding-docs (no engine on main yet; `kit/founding-docs.js` is planned in batch W4 for premise-inspector and founding-words-explorer). This tool keeps its amendment data (number, plain words, real text, principle, duty) as plain data in one marked block, `/* FOUNDING-DOCS DATA: begin */ ... /* end */`, so the family engine can take it later. Tool-only code: the meeting scenes, the step strip, the sort, the scale.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Try each slot until one sticks | Each wrong drop plays the slot-words hint; the end chart counts first-try sorts privately for the teacher, not shown as a score to the child. |
| Steps | Leave the strip in any order | The strip checks dates and swaps back with "Which came first?" |
| Limits | Always pick "ban it" | The narrator explains that banning the message isn't allowed; the child picks again. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Meeting scenes (whole), each waits.
2. `choose`; `strip`.
3. `sort`; each purpose (whole).
4. `weigh`; answers (whole). `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.3.3-5, D2.Civ.4.3-5 and D2.Civ.8.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Constitution signed September 17, 1787; Bill of Rights ratified December 15, 1791; Madison proposed amendments in 1789 | National Archives, "The Bill of Rights: How Did It Happen?" | Library of Congress, "Creating the United States: Bill of Rights" | yes |
| George Mason refused to sign because the Constitution had no bill of rights | National Archives, "George Mason's Objections" | Gunston Hall (George Mason's home museum), "George Mason" | yes |
| Massachusetts ratified on February 6, 1788, 187 to 168, with recommended amendments | Massachusetts Historical Society, "Massachusetts ratifies" | National Constitution Center, "Massachusetts ratification" | yes |
| The plain meaning of the 1st, 3rd, 4th, 5th, 6th and 8th Amendments | National Archives, Bill of Rights transcript | National Constitution Center, Interactive Constitution | yes |
| Quartering soldiers in colonists' homes (Quartering Acts 1765 and 1774) | Library of Congress, "Quartering Act" | Encyclopaedia Britannica, "Quartering Act" | yes |
| Governments may set time, place and manner rules for marches; false statements that harm someone are not protected | National Constitution Center, Interactive Constitution, First Amendment | U.S. Courts, "What does free speech mean?" | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-09): 187 + 168 = 355 delegates; the four steps sort as 1787, 1787 to 1788, 1789, 1791; each of the eight scenarios maps to exactly one of the six slots and each slot gets at least one; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 six slots in a row; at 680x425 a two-by-three grid.
2. The meeting plays and the four-step strip checks the order. (D2.Civ.3.3-5, D2.Civ.4.3-5)
3. Each scenario sorts to its amendment and shows purpose, principle and duty. (D2.Civ.8.3-5)
4. The two limits cases accept a rule and explain it. (D2.Civ.8.3-5)
5. The real amendment text is a tap away on every slot.
6. Class vote shows each scenario before the sort.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flipping or tilting; no network requests.

## Open questions
- The module lists D2.Civ.5.3-5 (structure of government), which a scenario sort can't teach well (default used: it moves to bill-to-law-board-game as a federal-and-state contrast card; module code list left for Cory).
