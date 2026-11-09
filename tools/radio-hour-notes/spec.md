# Radio Hour Notes

## One idea
The student is the note-taker at a kids' radio show: they listen to a field trip report, pause to jot the main points, call in with the question that asks for more, then sort a guest's claims about a longer recess into bins by what holds each one up (a reason, evidence, or nothing at all), and at the end the host reads a summary from the student's own notes and replays the one unbacked claim the student believed, so they learn that listening well means catching both what a speaker says and how they back it up.

## Not like
- claim-court (5, concept): an author's written claims on trial. Here spoken claims, heard, not read.
- class-phone-call (K-2, concept): asking questions on a call. Here notes, follow-up questions and judging support.
- main-idea-pinboard (3-5, concept): main idea in written text. Here in a spoken segment.
- planetarium-guide (3-5, spec): being the speaker. Here the listener.
- headline-writer (3, spec): main idea of a printed news story. Here of radio audio, with reasons and evidence.

## Who and how
- Grades 3-5, ELA, module "Listening for Main Points and Reasons" (Speaking and Listening). Standards: SL.3.2, SL.3.3, SL.4.2, SL.4.3, SL.5.2, SL.5.3.
- Driver: one student with headphones, or a class listening together (tool.json `driver: "student"`). Listening is the task: the transcript toggle is off by default and a teacher note says when to turn it on (a student who needs it).
- Grade picker (3, 4, 5) picks the segment version: grade 3 segments run about 90 seconds, grade 5 about 3 minutes, with more points and a chart. tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the notepad and the claim bins.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.3.2 | Segment 1: pause and pick or type the main points and key details, then compare with the host's recap | the notepad beside the recap | 2 |
| SL.3.3 | Call-in break: choose the follow-up question that asks for more, hear the answer | four question cards and the answer | 3 |
| SL.4.2 | Paraphrase: the show page's picture and chart, put into the student's own words from tiles or typed | the show page and the paraphrase box | 4 |
| SL.4.3 | Segment 2: name the reason or evidence the guest gives for each point | claim cards in bins | 5 |
| SL.5.2 | Summarize each segment from the notes in two or three sentences | the summary card | 6 |
| SL.5.3 | Summarize the guest's points and explain which reasons and evidence support each | the bins plus a "best backed" pick with why | 5, 6 |

## Screens and modes
Header (kit): title "Radio Hour Notes"; `Show`, `Transcript` (off); `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A radio studio with an ON AIR light, a notepad, and host Jada at the mic. First hint: "Tap Play to start the show." The first tap starts the show's opening; the welcome is queued after it (`welcomeAfter: true`).

**Segment 1: Field Trip Report.** Reporter Sam reports on a class trip to the Maple Marsh Nature Center. Player: Play, Pause, back 10 seconds (all 44 px). When paused, the notepad offers point cards (8 cards: 3 main points, 3 details, 2 off-topic remarks like the bus being late) or a typing line. After the segment, the host's recap plays and the notepad marks which recap points the student caught (cards match by id; typed notes match by key-word groups, generous with word forms). Missed points get a "listen again" button that jumps to the spot.

**Call-in break.** Four question cards for the reporter: one already answered in the report, one off topic, one yes-or-no, and one that asks for more ("How does the marsh clean the water?"). Picking one plays its answer from the reporter; the off-topic and already-answered ones get the host's gentle reply ("Sam said that at the start. Want to hear it again?"), then the student can pick again.

**Show page.** The station's web page for the segment: a picture (a marsh diagram) and a small bar chart the reporter mentioned (birds counted on the trip). Grade 4 and up: paraphrase from tiles (one copies the words, one changes the meaning, one says it in new words) or type.

**Segment 2: The Guest.** Riley, a fifth grader, argues for a longer recess. Six claim cards appear as Riley speaks; the student drops each into a bin: backed by a reason, backed by evidence, not backed. Data per claim. Grade 5 also picks the best-backed claim and the tile that says why.

**Wrap.** The host reads a summary built from the student's notepad. If the student put an unbacked claim in a backed bin, the host replays that clip with "Listen again. What held this one up?"

At 1366x768 the player, notepad and bins fit; at 680x425 the notepad is a drawer.

## Content
**Segment 1 (grade 3 version, written for Curio Class):** main points: the marsh is a home for many animals; marsh plants slow water down and help clean it; kids counted birds for a science project. Details: they saw a great blue heron; cattails grow at the edges; they counted 43 birds of 9 kinds. Off-topic: the bus was late; lunch was sandwiches. Grade 4 adds the chart; grade 5 adds a fourth point (marshes can soak up floodwater) and two details.
**Segment 2 claims (Riley):**
1. "Kids need to move a lot every day. Doctors say kids should get an hour of activity a day." (evidence)
2. "Recess is the best part of the day." (not backed)
3. "We could focus better after we play, because our brains get a break." (reason)
4. "At our school, 18 of 24 kids in my class said they'd like a longer recess. I asked them." (evidence; Riley's own count, called made up in the teacher note)
5. "Everybody knows longer recess is better." (not backed)
6. "A longer recess means more time to solve arguments and make friends, because we practice playing fair." (reason)
The grade 5 best-backed pick is claim 1 (an outside source) with the tile "It comes from doctors, not just Riley."

## Interactions in detail
- Every tap acts at once; a new line stops the old one, except the show audio, which pauses when a voice line plays and resumes after.
- Pausing never loses place; the back button jumps 10 seconds.
- Bins accept any card and can be changed until `Done`; then each card shows its bin's reason ("Riley named who said it: that's evidence.").
- Transcript, when on, highlights the line playing.

## Look
- Accent `--brand` #a8431a on-air orange (header, the ON AIR sign, bins); gold #f4c542 (the active notepad line, the light glow); paper #fdf6f1; ink #26150c; muted #665449. Scene: a cozy kids' radio studio.
- Contrast (WCAG 2.1, computed): white on brand 6.03:1; brand on paper 5.64:1; ink on paper 16.43:1; muted on paper 6.70:1; ink on gold 10.80:1.
- Never color alone: bins have names and icons (a speech bubble for reason, a magnifier for evidence, an empty box for not backed).
- Different from this batch (gallery plum, planetarium navy, reading-table green, story teal).

## Art
- People art goes to Gemini: host Jada (a Black girl about 12 at a mic), reporter Sam (an East Asian boy about 11 with a field notebook), guest Riley (a white girl about 10 in a sports jersey); 4 poses each (talk, listen, laugh, think), "illustrated kid radio host <description> <pose>, warm illustrated style, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): studio (1), "A cozy kids' radio studio with an ON AIR light and microphones, soft gouache, no text"; 16:9. Marsh diagram (1) and marsh photo-style scenes (3); 4:3.
About 17 images. Drawn in code: player, notepad, bins, chart.

## Voice
Show audio is produced from bank voices: `lively-host` as Jada (also the tool's guide voice), `clear-teacher` as Sam, `casual-peer` as Riley; each grade version is its own recording. All three are unique in this batch. `Curio.voice` with `scope: () => state.grade + ':' + state.segment`, `welcomeAfter: true`.
- how `welcome`: "Welcome to Radio Hour! You're our note-taker today. Pause when you hear something important and jot it down."
- how `pauseHow`: "Paused. Pick a card for your notepad, or type a note. Then tap Play."
- event `recap`: "Here's my recap. Let's see what you caught."
- how `callHow`: "Call-in time! Which question asks Sam for more?"
- event `callRedirect`: the host's reply for the card.
- how `binHow`: "Drop each of Riley's claims in a bin. What holds it up?"
- event `binReason`: the card's reason.
- event `replay`: "Listen again. What held this one up?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Notepad | Pick every card | The recap marks off-topic cards as "not a main point" and details as details; the notepad shows the difference. |
| Call-in | Try all four | Allowed; each wrong one plays a reply that teaches why. Not scored. |
| Bins | One bin for all | Two claims per bin; one bin for all gets four wrong with reasons (checked). |
| Best-backed | Guess | One of six; the why tile is needed too. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Play: show opening, `welcome` (queued, first time).
2. Pause: `pauseHow` (first time). Segment end: `recap`.
3. Call-in: `callHow`; wrong pick: `callRedirect`.
4. Segment 2: `binHow`; Done: `binReason` per card; wrap: summary, then `replay` if needed.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.3.2 to SL.5.3 wording | thecorestandards.org, Speaking and Listening Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Children and teens should get about 60 minutes of physical activity a day | CDC, physical activity guidelines for children | WHO, physical activity fact sheet | yes |
| Recess helps children's social skills and readiness to learn | American Academy of Pediatrics, "The Crucial Role of Recess in School" (2013) | CDC, strategies for recess in schools | yes |
| Wetland plants slow water and help filter it; wetlands can hold floodwater | US EPA, why wetlands are important | USGS, wetlands water science | yes |
| Great blue herons and cattails are common in North American marshes | Cornell Lab of Ornithology, All About Birds, great blue heron | US Fish and Wildlife Service, wetland plants | yes |
Backed twice: 5. Cut: 0.

Sensitivity note: kid characters in people art go to the fresh-agent review; Riley's survey numbers are labeled as her own count.

Checks run (Python, scratchpad b9, 2026-11-08): two claims per bin; one-bin answer gets 4 of 6 wrong; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the player, notepad and bins fit; at 680x425 the notepad is a drawer.
2. Pausing offers cards or typing; the recap marks caught and missed points with jump-back buttons. (SL.3.2)
3. The call-in plays answers and redirects. (SL.3.3)
4. The show page paraphrase works from tiles or typing. (SL.4.2)
5. Claims sort into three bins with reasons after Done; grade 5 picks the best-backed claim and why. (SL.4.3, SL.5.3)
6. The wrap reads a summary from the notes and replays a misjudged claim. (SL.5.2)
7. Each grade plays its own recordings; the transcript toggle is off by default.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the ON AIR light doesn't blink; no network requests.

## Open questions
- None for Cory.
