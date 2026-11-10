# School Fix-It Meeting

## One idea
The child picks one of three school problems from the hallway bulletin board (a lunch line so long that first graders have ten minutes to eat, a crowded hallway after recess, a playground with no shade), asks a first grader, a fifth grader, a lunch worker and the custodian "Why does this matter to you?" and sorts what they hear (some answers surprise: the trays are washed by hand because the dishwasher broke), then chairs a fix-it meeting with illustrated classmates, calling on people in turn, handling a shout-out, asking someone to build on an idea and merging two half-plans into a better one, and finally runs a vote and writes the plan for the principal with who it helps and who said so, so a third grader learns why a question matters to different people and how a group decides and acts together.

## Not like
- town-council (2, spec): a town council and one lot. Here a class meeting about a school problem, with a survey first.
- pool-repair-vote (3, spec): town policy and paying for it. Here a class deciding and bringing a plan to the principal.
- playground-rules (K, spec): why rules matter. Here meeting rules in use, and combining ideas.
- ripple-street (3, spec, this batch): one person's choices. Here a group decision.

## Who and how
- Grade 3, Social Studies (Inquiry and Civics), module "School Fix-It Meeting". Standards: D1.1.3-5 (explain why compelling questions are important to others, e.g. peers, adults), D2.Civ.9.3-5 (use deliberative processes when making decisions or reaching judgments as a group), D4.8.3-5 (use a range of deliberative and democratic procedures to make decisions about and act on civic problems in their classrooms and schools), AASL.Collaborate (III.A.2 developing new understandings through engagement in a learning group; III.B.2 establishing connections with other learners to build on their own prior knowledge and create new knowledge).
- Format: the idea card changes it from showdown to roleplay, because a solo child needs illustrated classmates and adults to survey and deliberate with; a real class meeting is the extra.
- Driver: one child alone by default; the class version uses the projector (tool.json `driver: "either"`). `Read` reads every line. Controls 44 px or more.
- Four parts: Pick, Survey, Meeting, Plan. Extra: Real meeting (printable survey cards, meeting rules poster, a vote counter). tool.json `modes: ["Fix-it", "Real meeting"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D1.1.3-5 | Ask four people "Why does this matter to you?" and sort each answer by who it matters to and why | four answer cards on a "Why it matters" board, sorted under Time, Fun, Work, Safety or Mess | 2 |
| D2.Civ.9.3-5 | Chair the meeting: call on raised hands in turn, stop a shout-out with the rule, ask "Can someone build on that?" | the meeting table with hands, the rules poster lighting the rule in use | 3 |
| AASL.Collaborate | Merge two half-plans into one by dragging the strong part of each onto a new plan card | two half-plan cards and the merged card | 4 |
| D4.8.3-5 | Hold the vote and write the plan for the principal: what we'll do, who it helps, who said so | the vote count and the plan letter | 5 |

## Screens and modes
Header (kit): title "School Fix-It Meeting"; `Fix-it`, `Real meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A hallway bulletin board with three problem cards: "The lunch line is too long", "The hallway is jammed after recess", "There's no shade on the playground". The welcome is queued (`welcomeAfter: true`): "Our school has problems we can fix together. Which one should we fix first? Tap a card." First hint: "Tap a problem card."

**Pick.** Tapping a card reads it and opens `Fix this one`. Each problem has its own survey, proposals and plan; the lunch line is shown in full here and the other two follow the same shape (see Content).

**Survey (focus: one person at a time).** At 1366x768 four people stand along the hallway and the "Why it matters" board sits right; at 680x425 one person shows at a time with the board as a sheet.
- The child taps a person, then `Ask` ("Why does this matter to you?"). Lunch line answers:
  - Leo, first grader: "By the time I get my tray, I only have ten minutes to eat. I'm still hungry at recess."
  - Maya, fifth grader: "We go last, so we wait the longest and miss part of recess."
  - Mrs. Duarte, lunch worker: "Our dishwasher broke. We wash trays by hand, so we run out of clean trays and the line stops." (the surprise)
  - Mr. Fox, custodian: "When kids rush, food spills. I clean it up during recess."
- The child drags each answer card under one of five reasons: Time, Fun, Work, Safety, Mess. Leo: Time; Maya: Fun; Mrs. Duarte: Work; Mr. Fox: Mess. (Safety stays empty here; it is used by the hallway problem.) After the four: "The same problem matters to each person for a different reason. Mrs. Duarte's answer changes what we should fix!"

**Meeting (focus: the table).** Five classmates sit with the child at the head. A rules poster: "Raise your hand. One voice at a time. Build on ideas: Yes, and..." 
- Hands go up two at a time; the child taps a raised hand to call on that person. Proposals:
  - Ana: "Let each grade come to lunch at a different time."
  - Ben: "Put a grab-and-go table with milk, fruit and sandwiches by the door."
  - Cy: "Use paper trays so they never run out." Kim: "But then we'd throw away a lot of trash every day."
- Shout-out: while Ana is speaking, Ben shouts "Mine's better!" The child taps the poster rule `One voice at a time`; Ben says "Sorry, Ana. Go ahead." If the child calls on Ben instead, Ana stops, and the narrator: "Ana didn't get to finish. Which rule helps?"
- Build on: after Ana and Ben, the child taps `Can someone build on that?`; Kim: "Yes, and if first grade goes first, they get the full time to eat."
- Merge: two half-plan cards (Ana's different times, Ben's grab-and-go table) and the child drags one strong part of each onto a new plan card: "First graders go first, and a grab-and-go table helps the line move while the trays get washed." Cy's paper trays get the trash concern, and the group sets it aside unless no other plan works.

**Plan (focus: the vote and the letter).** Three plans on the board: the merged plan, Ana's alone, Ben's alone. `Vote` asks each classmate and the child; with the merged plan on the board it wins 4 to 1 to 1 (Ben votes for his own plan, Cy for Ana's; the others choose the merged one). If the child didn't merge, the vote splits 2, 2, 2 and the narrator: "No plan has most of the votes. Can two plans become one?" and the merge step returns.
- The letter to Principal Shah fills from the work: what we'll do (the plan), who it helps (from the survey board), who said so (the four people and the meeting). The child picks one sentence to open the letter from three. `Print` prints the letter, the board and the vote.

**Real meeting (extra).** Printable survey cards with the question and space for four answers, the rules poster, three blank proposal cards and a projector vote counter.

## Content
- Three problems, each with four survey answers and five reasons, three proposals, one shout-out, one build-on line and one merge:
  - Lunch line: as above.
  - Hallway: a kindergartner (gets bumped, Safety), a fourth grader (late to class, Time), a teacher (lessons start late, Work), the nurse (more scraped knees, Safety). Proposals: one-way hallway; grades come in from recess at staggered times; tape lines on the floor. Merge: one-way with staggered times.
  - Shade: a second grader (too hot to play, Fun), a fifth grader (slide burns in May, Safety), a recess aide (kids crowd the one tree, Safety), the PTA president (trees cost money, Work). Proposals: plant trees; a shade sail over the slide; move recess earlier on hot days. Merge: shade sail now, trees for later.
- Principal Shah, the school and everyone in it are made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Fix this one` shows after a card is read. `Ask` shows after a person is tapped. `Can someone build on that?` shows after two proposals. `Vote` shows after the merge (or after all proposals if the child skips it).
- Keyboard: Tab between people, hands and cards; Enter to ask, call on, pick up and drop.
- With Motion off hands appear raised without moving.

## Look
- Accent `--brand` #6a3d9a meeting plum (header, the board, the rules poster); gold #f4c542 (a raised hand, the rule in use, the merged card); paper #f6f2fa; ink #1e1030; muted #5c5466.
- Contrast (WCAG 2.1, computed): white on brand 7.64:1; brand on paper 6.92:1; ink on paper 16.21:1; muted on paper 6.52:1; ink on gold 11.02:1.
- Never color alone: reasons carry icons and words; a raised hand also shows a number for turn order.
- Different from this batch (ripple blue, barter ochre, skateboard berry, valley olive).

## Art
- People art goes to Gemini with `people: true`: twelve survey people across the three problems (1 pose each; cutout yes); five classmates Ana, Ben, Cy, Kim, Jay (3 poses each: hand up, speaking, listening; cutout yes); Principal Shah (1 pose).
- Local FLUX (`scripts/localart.py`): the hallway bulletin board (1, 16:9); the lunch room, the hallway, the playground (3, 16:9); the meeting table (1, 16:9).
- Drawn in code: answer cards, the reasons board, the rules poster, proposal and plan cards, the vote count, the letter.
About 33 images.

## Voice
Eight bank voices, each unique in this batch: `clear-teacher` as the narrator; for the lunch-line survey `soft-breath` (Leo), `big-sister` (Maya), `gentle-storyteller` (Mrs. Duarte), `friendly-dad` (Mr. Fox); classmates `easy-coach` (Ana), `lively-host` (Ben), `curious-librarian` (Kim). Cy and Jay are read by the narrator. The other two problems' people reuse these voices by role. `Curio.voice` with `scope: () => state.problem + ':' + state.part + ':' + state.person`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `ask`: "Tap a person, then tap Ask."
- event, whole, each answer (in the person's voice).
- how `sort`: "Drag the answer to the reason it matters."
- event, whole, `surprise`: "The same problem matters to each person for a different reason."
- how `call`: "Tap a raised hand to call on someone."
- event, whole, each proposal and the shout-out.
- how `rule`: "Tap the rule that helps."
- how `build`: "Tap Can someone build on that?"
- how `merge`: "Drag the best part of each plan onto the new card."
- how `vote`: "Tap Vote."
- event, whole, the count; `split` if no plan has most votes.
- how `letter`: "Pick a first sentence for the letter."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the survey and reasons board, the meeting table with hands and turn order, the rules poster, the merge card, the vote and the letter builder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reasons sort | Put every answer under Time | Each answer has one right reason; a wrong drop replays the key words. |
| Turn-taking | Call on the shouter | Ana stops; the narrator asks which rule helps, and the meeting waits for it. |
| Merge | Skip it | The vote splits 2, 2, 2 and the merge step returns. |
| Merge | Drag Cy's paper trays | The trash concern plays; it can't be the strong part while two others work. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Pick: the card read; survey: `ask`; each answer (whole), waits; `sort`; after four: `surprise` (whole).
2. Meeting: `call`; proposals (whole); shout-out (whole); `rule`; `build`; build line (whole); `merge`.
3. Plan: `vote`; count (whole) or `split`; `letter`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D1.1, D2.Civ.9 and D4.8 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| AASL Collaborate competencies III.A.2 and III.B.2 | AASL Standards Framework for Learners (2018) | data/standards/aasl-2018.txt | yes |
| Students with less than 20 minutes seated lunch eat less of their meal; at least 20 minutes is advised | CDC, "Making time for school lunch" | Cohen et al., Journal of the Academy of Nutrition and Dietetics, 2016, lunch time and intake | yes |
| Classroom meetings use turn-taking, building on ideas and voting to reach group decisions | Responsive Classroom, "Morning Meeting" and class meetings | Teaching Tolerance (Learning for Justice), class meeting guides | yes |
| Shade structures and trees lower playground surface temperatures and burn risk | U.S. EPA, "Heat island" and shade | American Academy of Dermatology / Skin Cancer Foundation, shade at schools | yes |
| One-way hallways and staggered transitions ease crowding | National Association of Elementary School Principals, hallway transition guidance | Wikipedia, Crowd control (checked 2026-11-09) | partly |
Backed twice: 5. Cut: 1. The hallway claim rests on one strong source; it stays as a reasonable classroom proposal, not a fact the tool states.

Checks run (Python, scratchpad r6, 2026-11-09): each problem has four answers and three proposals; the lunch reasons are four different reasons; the vote is 4, 1, 1 with the merge and 2, 2, 2 without, over six voters; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 people and board fit; at 680x425 one person shows at a time.
2. Each answer sorts only to its reason, and the surprise line plays. (D1.1.3-5)
3. Calling on the shouter pauses the meeting until the rule is tapped. (D2.Civ.9.3-5)
4. The merged card takes one part of each half-plan. (AASL.Collaborate)
5. The vote, the letter and the print include who it helps and who said so. (D4.8.3-5)
6. `Fix this one`, `Ask`, `Can someone build on that?` and `Vote` are never named before they show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving hands; no network requests.

## Open questions
- None for Cory. (The format change from showdown to roleplay comes from the idea card.)
