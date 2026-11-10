# Constitutional Convention

## One idea
The child is a delegate in Philadelphia in the summer of 1787, from small Delaware or large Virginia, sitting in the Assembly Room with the windows shut for secrecy; they start from what was broken under the Articles of Confederation (no power to tax, no national courts, no leader to carry out laws, any change needing every state), then work through six sessions (the Virginia and New Jersey plans, the Connecticut Compromise, the presidency, the courts, slavery's compromises told plainly, and the powers and limits of each branch), reading two plans, hearing delegates, and voting or proposing a deal while two meters move on every vote: their state's interests and the principles of the Declaration; the finished plan becomes a diagram of three branches with their powers and checks, a ratification round follows, and "still here today" cards trace popular sovereignty, separation of powers and federalism into government now, with a side card naming who wasn't in the room, so an eighth grader learns why the Constitution was written, how it is structured, the powers and limits of each branch, and how interests and principles both shaped it.

## Not like
- agora-assembly (6, spec): direct democracy in Athens. Here representatives writing a plan.
- motion-on-the-floor (8, concept): running one meeting by rules. Here a summer of bargains.
- founding-words-explorer (9, spec): reading the finished text closely. Here making it.
- reconstruction-amendments (8, concept): changing the Constitution after the Civil War. Here writing it.

## Who and how
- Grade 8, Social Studies (Civics), module "Creating the Constitution". Standards: D2.Civ.3.6-8 (examine the origins, purposes, and impact of constitutions, laws, treaties, and international agreements), D2.Civ.4.6-8 (explain the powers and limits of the three branches of government, public officials, and bureaucracies at different levels in the United States and in other countries), D2.Civ.5.6-8 (explain the origins, functions, and structure of government with reference to the U.S. Constitution, state constitutions, and selected other systems of government), D2.Civ.10.6-8 (explain the relevance of personal interests and perspectives, civic virtues, and democratic principles when people address issues and problems in government and civil society), D2.Civ.8.6-8 (analyze ideas and principles contained in the founding documents of the United States, and explain how they influence the social and political system; moved here from agora-assembly per the idea card).
- Format: roleplay. Driver: one child alone, or the class split into state delegations (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- What's broken, six sessions, the diagram, ratification, still here today. Extra: State delegations (groups vote as states, one vote each, as the Convention did). tool.json `modes: ["Delegate", "State delegations"]`, `minutes: "35-45"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.3.6-8 | Match each Articles problem to the fix the Convention made | the "what's broken" list with fixes clipped on | 2 |
| D2.Civ.10.6-8 | Vote or propose a deal in each session and read both meters | the interests meter (your state) and the principles meter (the Declaration) with reason lines | 3 |
| D2.Civ.4.6-8 | Give each branch its powers and the checks on it | the three-branch diagram with power and check tags | 4 |
| D2.Civ.5.6-8 | Compare the finished structure with the Articles side by side | the two diagrams | 4 |
| D2.Civ.8.6-8 | Link each principle to a "still here today" card | three principle cards matched to today's examples | 5 |

## Screens and modes
Header (kit): title "Constitutional Convention"; `Delegate`, `State delegations`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Assembly Room of the Pennsylvania State House: green-covered tables, closed windows, George Washington's chair at the front. On the table, the Articles of Confederation and a list headed "What's broken." Two delegate badges: Delaware, Virginia. The welcome is queued (`welcomeAfter: true`): "It's May 1787 in Philadelphia. The country's first plan of government isn't working. You're a delegate. Pick your state." First hint: "Tap a state badge."

**What's broken (focus: the list, D2.Civ.3.6-8).** At 1366x768 the room fills the screen with the list as a side panel; at 680x425 the list is a sheet.
- Under the Articles: Congress could ask states for money but not tax; no national courts to settle disputes between states; no executive to carry out laws; each state one vote; changing the Articles needed every state to agree. A card on Shays' Rebellion in Massachusetts (1786 to 1787) shows why some leaders worried.
- As sessions finish, the child clips each fix onto its problem.

**Sessions (focus: the plans and the meters, D2.Civ.10.6-8).**
1. The Virginia Plan and the New Jersey Plan: representation by population or one vote per state. Delaware's delegates (John Dickinson, George Read) and Virginia's (James Madison, Edmund Randolph) explain.
2. The Connecticut Compromise (July 16): a House by population and a Senate with two per state; it passed by one state's vote.
3. The presidency: one person or a council; how chosen (the Electoral College as a compromise).
4. The courts: a Supreme Court and courts Congress may create; judges serve during good behavior.
5. Slavery's compromises, told plainly: the three-fifths clause counted three of every five enslaved people for representation and taxes, giving slaveholding states more seats; Congress could not ban the slave trade before 1808; a fugitive slave clause. Delegates spoke against slavery and for it; the narrator names that enslaved people had no voice in the room. No images of enslaved people.
6. Powers and limits: Congress's listed powers, the president's veto, Congress's power to override, the Senate's approval of treaties and judges, impeachment.
- In each session, the child votes for a plan or picks a deal from tiles. The interests meter moves by what helps their state (Delaware gains from equal votes; Virginia from population); the principles meter by consent of the governed, equality and liberty. Some votes help one and hurt the other, and the reason lines say so.

**The diagram (D2.Civ.4.6-8, D2.Civ.5.6-8).** The child builds the three branches: drag power tags (make laws, carry out laws, decide cases, veto, override, approve judges, impeach) to each branch, and check arrows between them. Beside it, the Articles' one-branch diagram for comparison.

**Ratification.** Nine of thirteen states needed: Delaware first (December 7, 1787, unanimous), New Hampshire ninth (June 21, 1788), Virginia close behind after a hard debate. A card on George Mason, a Virginia delegate who refused to sign without a bill of rights, and the promise that led to the Bill of Rights.

**Still here today (the aha, D2.Civ.8.6-8).** Three principles matched to today: popular sovereignty (elections for the House, and since 1913 for the Senate); separation of powers (a veto and an override in recent years); federalism (states and the nation each with their own powers). Narrator: "They bargained for their states and argued over principles. The plan they made still runs the country, and later Americans changed it to include more people."

**Who wasn't in the room.** A side card: no women, no Native nations, no enslaved people, no free Black Americans among the delegates; Rhode Island sent no one.

**The end.** The diagram, both meters' record, the fix list and the principle cards. `Print` prints them.

**State delegations (extra).** Groups vote as states, one vote each, as in the real Convention.

## Content
- The Articles problem list with fixes, six sessions with two plans, delegate cards and deal tiles, two meters (made for this game), the diagram with power and check tags, ratification cards, three principle cards, the side card.
- The meters are made up and labeled; delegates, dates, votes and clauses are real, quoted only in short phrases from the Constitution.
- Founding-docs data (clause, plain words, real text, principle) sits in one marked block for the family engine.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sessions go in order; each needs a vote or a deal before the next.
- The diagram accepts tags only where the Constitution puts them; a wrong drop plays "Which branch does this? Check Article I, II or III."
- Keyboard: Tab to badges, plans, tiles, meters, tags and cards; Enter to vote, pick and drop.
- With Motion off meters jump.

## Look
- Accent `--brand` #23395b Philadelphia navy (header, the diagram, session banners); gold #f4c542 (the vote in hand, a matched principle); paper #f3f5f9; ink #0a1324; muted #535866.
- Contrast (WCAG 2.1, computed): white on brand 11.62:1; brand on paper 10.64:1; ink on paper 17.00:1; muted on paper 6.51:1; ink on gold 11.41:1.
- Never color alone: the two meters carry labels and numbers; branches carry names and icons.
- Different from this batch (printer's sepia, archive green, canal blue, signal orange).

## Art
- Public domain: the signed Constitution's first page (National Archives); Howard Chandler Christy's "Scene at the Signing" (U.S. Capitol, public domain); the Articles of Confederation (National Archives). Each with credit.
- Local FLUX (`scripts/localart.py`): the Assembly Room (1, 16:9).
- People art goes to Gemini with `people: true`: Madison, Randolph, Dickinson, Read, Washington, Mason, Roger Sherman, Benjamin Franklin (8; cutout yes), from period portraits.
- Drawn in code: the meters, the diagram, the fix list, the ratification map.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the narrator; `calm-professor` as the delegates' cards. `Curio.voice` with `scope: () => state.mode + ':' + state.session + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `fix`: "Clip each fix onto the problem it solves."
- event, whole, each session's plans and delegate cards.
- how `vote`: "Vote for a plan or pick a deal."
- event, whole, each meter reason.
- how `diagram`: "Drag each power to its branch."
- event, whole, ratification cards.
- how `today`: "Match each principle to today."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
founding-docs (no engine on main yet; `kit/founding-docs.js` is planned for premise-inspector and founding-words-explorer). This tool keeps its clause data (article and section, plain words, short real text, principle, branch) as plain data in one marked block, `/* FOUNDING-DOCS DATA: begin */ ... /* end */`, so the family engine can take it later. Tool-only code: the room, sessions, meters, the diagram, ratification, the principle cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Votes | Always vote for your state | The principles meter falls and reason lines say why; the end shows both records. |
| Diagram | Drag tags at random | Each tag checks its branch with the Article hint. |
| Principles | Match at random | Each card checks; a miss names the principle's meaning. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `fix`.
2. Session plans and delegates (whole), each waits; `vote`; meter reasons (whole).
3. `diagram`; ratification (whole).
4. `today`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.3.6-8, D2.Civ.4.6-8, D2.Civ.5.6-8, D2.Civ.10.6-8 and D2.Civ.8.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Weaknesses of the Articles of Confederation; Shays' Rebellion | National Archives, "Articles of Confederation" | Library of Congress, "Creating the United States: Road to the Constitution" | yes |
| Virginia and New Jersey Plans; the Connecticut Compromise of July 16 passed by one state | National Archives, "The Constitution: How Did It Happen?" | U.S. Senate, "The Great Compromise" | yes |
| The three-fifths clause, the 1808 slave-trade clause and the fugitive slave clause | National Archives, Constitution transcript (Art. I sec. 2 and 9, Art. IV sec. 2) | National Constitution Center, Interactive Constitution | yes |
| Powers and checks of the three branches | National Archives, Constitution transcript | National Constitution Center, Interactive Constitution | yes |
| Delaware first to ratify (December 7, 1787, unanimously), New Hampshire ninth (June 21, 1788) | National Archives, "Observing Constitution Day: Ratification" | Delaware Public Archives, "Delaware: The First State" | yes |
| George Mason refused to sign without a bill of rights | George Mason's Gunston Hall, "Objections to the Constitution" | National Archives, "The Bill of Rights: How Did It Happen?" | yes |
| Rhode Island sent no delegates | National Archives, "Meet the Framers" | Library of Congress, "Creating the United States" | yes |
| Senators elected by the people since the 17th Amendment (1913) | National Archives, 17th Amendment | U.S. Senate, "Direct Election of Senators" | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: slavery's compromises are told plainly with the Constitution's own words and their effect on representation; the narrator names that enslaved people had no voice; no images of enslaved people. A fresh-agent read of session 5 is needed before build.

Checks run (Python, scratchpad r14, 2026-11-09): dates in order (May 25 opening, July 16 compromise, September 17 signing, December 7 Delaware, June 21 New Hampshire); 9 of 13 states needed; 1808 minus 1787 is 21 years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 room and list; at 680x425 sheet.
2. Each Articles problem gets its fix. (D2.Civ.3.6-8)
3. Six sessions move both meters with reasons. (D2.Civ.10.6-8)
4. The diagram places powers and checks and compares with the Articles. (D2.Civ.4.6-8, D2.Civ.5.6-8)
5. Principles match today's examples. (D2.Civ.8.6-8)
6. State delegations vote one per state.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: meters jump; no network requests.

## Open questions
- Sensitivity flag: slavery's compromises at the Convention (default used: the Constitution's words and effects told plainly, no images of enslaved people, fresh-agent read before build).
- Module change: D2.Civ.8.6-8 is added here from agora-assembly, as the idea card proposes (default used: added; agora-assembly's spec not touched).
