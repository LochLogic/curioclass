# Motion on the Floor

## One idea
The child chairs a student club meeting to decide how to spend $600 from the club's bake sale, gavel in hand: they follow the agenda, recognize speakers, take a motion and a second, handle an amendment (voted on before the main motion), keep debate fair when one member keeps interrupting and two quiet members never get the floor, call the question, and count the vote, while a fairness meter and a rules meter both move; then three short replays show the same kind of choice at a city council (public comment and open meeting rules), a school board (a public agenda posted ahead, a vote in public) and a state legislature (a bill through committee, two chambers and the governor), and a compare board names how each protects the public's voice, so an eighth grader learns to use democratic procedures to decide, to apply civic virtues in school, and to tell apart how different bodies make decisions.

## Not like
- agora-assembly (6, spec): ancient direct democracy. Here a modern club meeting by rules.
- constitutional-convention (8, spec): writing a plan of government. Here running a meeting.
- levers-of-power (8, spec): choosing where to act on a problem. Here how a group decides.
- shaping-our-week (8, spec): groups that shape a family's week. Here how one group decides.

## Who and how
- Grade 8, Social Studies (Civics and Taking Informed Action), module "Motion on the Floor". Standards: D4.8.6-8 (apply a range of deliberative and democratic procedures to make decisions and take action in their classrooms and schools, and in out-of-school civic contexts), D2.Civ.7.6-8 (apply civic virtues and democratic principles in school and community settings), D2.Civ.11.6-8 (differentiate among procedures for making decisions in the classroom, school, civil society, and local, state, and national government in terms of how civic purposes are intended).
- Format: roleplay. Driver: one child alone, or the class running a real meeting with the tool as a guide (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- The club meeting (seven agenda steps), three replays, the compare board. Extra: Real meeting (the tool shows the chair's script and next step while the class meets). tool.json `modes: ["Club meeting", "Real meeting"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D4.8.6-8 | Pick the chair's right next step at each point (recognize, state the motion, take the amendment first, call the question, count) | the agenda and the motion strip showing where the meeting is; the rules meter | 2 |
| D2.Civ.7.6-8 | Handle fairness moments (an interrupter, two members not heard, a tie) | the fairness meter and the members' faces; a reason line | 3 |
| D2.Civ.11.6-8 | Watch three replays and fill the compare board (who decides, who can speak, how the public knows, how many votes) | the board with four columns: club, city council, school board, legislature | 4 |

## Screens and modes
Header (kit): title "Motion on the Floor"; `Club meeting`, `Real meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A classroom after school, desks in a horseshoe, eight club members (made for this game) with name tents, a gavel at the chair's desk, an agenda on the board: Call to order, Minutes, Treasurer's report, Old business, New business (spend the $600), Announcements, Adjourn. A sign-in sheet shows a quorum (5 of 8). The welcome is queued (`welcomeAfter: true`): "You're chair of the Garden Club. Today the club decides how to spend $600 from the bake sale. Tap the gavel to call the meeting to order." First hint: "Tap the gavel."

**The meeting (focus: the members and the motion strip, D4.8.6-8).** At 1366x768 the room fills the screen with the agenda and motion strip at the side; at 680x425 they're a bottom strip.
- Each step offers two or three chair actions; one is right and the others play why they aren't ("A motion needs a second before debate.").
- New business: Mia moves to spend all $600 on raised garden beds; Jordan seconds. The child states the question. Debate opens: Sam wants $200 for a field trip. Sam moves to amend to $400 for beds and $200 for the trip; Ava seconds. The child must take the amendment first. Then the amended motion.
- Rules: a motion needs a second; the chair states the question before debate; members speak when recognized; an amendment is voted before the main motion; closing debate early ("calling the question") needs a two-thirds vote; most motions pass by a majority of votes cast.
- The rules meter rises with right steps and falls with skipped ones.

**Fairness moments (D2.Civ.7.6-8).**
- Leo keeps interrupting: the chair can gavel and remind, recognize him in turn, or let it go (the fairness meter falls if let go).
- Priya and Ben have their hands up but haven't spoken: the chair can call on members who haven't spoken yet before those who have.
- A tie on the amendment: the chair's choices (a chair who is a member may vote; a tie means the motion fails); the child reads the rule and decides.
- Each moment plays a reason line, and the members' faces change.

**Replays (D2.Civ.11.6-8).** Three short scenes, each deciding something similar (spending money on a park, a school garden, a statewide grant for school gardens):
- City council: the agenda posted days ahead under the state's open meetings law; a public comment period; council votes in public.
- School board: a public agenda; board members vote; students can speak at public comment.
- State legislature: a bill goes to a committee hearing where the public can testify, passes one chamber, then the other, then goes to the governor (most states have two chambers; Nebraska has one).
- After each, the child fills its column on the compare board: who decides, who can speak, how the public knows, how many votes it takes.

**The compare board (the aha).** Four columns side by side. The child picks one way each body protects the public's voice. Narrator: "Rules aren't there to slow things down. They make sure everyone gets heard and everyone knows what was decided."

**The end.** The meeting's minutes (written automatically from the child's steps), both meters, and the compare board. `Print` prints them.

**Real meeting (extra).** A chair's script with the next step highlighted for a live class meeting.

## Content
- An agenda, eight members (made for this game) with lines, the motion and amendment, about twenty chair-step choices, three fairness moments, three replays, the compare board.
- The club, members, money and replays' places are made up and labeled; the procedures follow Robert's Rules of Order and real open-meeting and legislative processes.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each step waits for the chair's choice; wrong choices explain and let the child choose again.
- Vote counting is a tap per member's raised hand, with the total shown.
- Keyboard: Tab to chair actions, members and board cells; Enter to choose.
- With Motion off hands rise without animation and the gavel doesn't swing.

## Look
- Accent `--brand` #2e5e3e committee green (header, the agenda, the motion strip); gold #f4c542 (the current step, a member recognized); paper #f1f6f2; ink #0b1f11; muted #4f5a52.
- Contrast (WCAG 2.1, computed): white on brand 7.54:1; brand on paper 6.89:1; ink on paper 15.76:1; muted on paper 6.58:1; ink on gold 10.60:1.
- Never color alone: meters carry numbers and labels; the recognized member carries a ring and their name.
- Different from this batch (amendment indigo, mill brick, colonial leather, transit teal).

## Art
- Local FLUX (`scripts/localart.py`): the classroom set for the meeting (1, 16:9); a city council chamber (1, 16:9); a school board room (1, 16:9); a state legislative committee room (1, 16:9).
- People art goes to Gemini with `people: true`: eight club members, a council member, a board member, a legislator (11; cutout yes).
- Drawn in code: the agenda, motion strip, meters, vote count, compare board, minutes.
About 15 images.

## Voice
Two bank voices, each unique in this batch: `clear-teacher` as the parliamentarian coach and narrator; `casual-peer` as the club members' lines. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `step`: "Pick what the chair does next."
- event, whole, each member's line.
- event, whole, each reason line.
- how `fair`: "Pick how the chair handles this."
- event, whole, each replay.
- how `board`: "Fill this body's column on the board."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the agenda and motion strip state machine, member lines, the two meters, fairness moments, replays, the compare board, auto minutes.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Steps | Tap choices until one works | Each miss explains; the minutes record the steps taken, and the rules meter shows misses. |
| Fairness | Ignore the quiet members | The fairness meter falls and the end card names who wasn't heard. |
| Board | Fill every column the same | Each cell checks; "how many votes" differs for the legislature. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `step`; member lines (whole), each waits.
2. Reason lines (whole); `fair`.
3. Replays (whole), each waits; `board`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D4.8.6-8, D2.Civ.7.6-8 and D2.Civ.11.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Motion steps: second, chair states the question, debate when recognized, put the question, announce | Robert's Rules of Order Newly Revised, 12th ed. (2020), summarized at robertsrules.com | National Association of Parliamentarians, "Basic motions" | yes |
| Amendments voted before the main motion; closing debate needs two-thirds | Robert's Rules (12th ed.) | National Association of Parliamentarians | yes |
| A tie vote means the motion fails | Robert's Rules (12th ed.) | National Association of Parliamentarians | yes |
| State open meetings laws require public notice and public votes | Reporters Committee for Freedom of the Press, Open Government Guide | National Conference of State Legislatures, open meetings overview | yes |
| A bill goes through committee hearings, both chambers and the governor; Nebraska has one chamber | National Conference of State Legislatures, "How a bill becomes law" | Nebraska Legislature, "The Unicameral" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r15, 2026-11-09): $400 plus $200 is $600; quorum 5 of 8 is a majority; two-thirds of 8 voting is 6 votes (5.33 rounded up); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 room, agenda and strip; at 680x425 bottom strip.
2. The meeting runs with right steps, amendment first, and a counted vote. (D4.8.6-8)
3. Three fairness moments move the fairness meter with reasons. (D2.Civ.7.6-8)
4. Three replays fill the compare board. (D2.Civ.11.6-8)
5. Minutes print from the child's steps.
6. Real meeting shows the chair's script.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animation; no network requests.

## Open questions
None.
