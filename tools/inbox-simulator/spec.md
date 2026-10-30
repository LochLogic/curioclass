# Inbox Simulator

## One idea
Every email has two readers' reactions you can see: a register meter shows how formal your reply sounds against the zone that fits this person (a friend, a coach, a teacher, a job), and the person's next email shows whether you gave them the information they asked for, so a perfectly polite reply that forgets the day you can work still gets "Which days can you work?" back, and a perfect answer to a friend written like a cover letter gets "why so formal?? are you mad at me".

## Not like
- interview-simulator (cte 9-12, specced): answering a hiring manager's spoken questions with specific stories. Here written email only, about schedules, requests and replies; no interviews (overlap note).
- classroom-phrases-game (eld K-2, built): sixteen spoken classroom phrases. Here written messages, register and requested information at high school level.
- workplace-scenarios (cte 6-8, specced): choices at work that ripple through a day. Here each choice is a word or phrase and the result is the reader's reply.
- audience-shift-briefing (ela 9): one finding presented to three rooms. Here many short messages, each to one reader, and register is measured phrase by phrase.
- counterpoint-frames, is-the-historian-right, chart-narrator, definition-duel (eld 9-12, this group): academic language. This is the group's social and instructional language tool.

## Who and how
- ELD grades 9 to 12. Module: College and Career Language (Social and Instructional Language).
- Driver: a student alone. 20 to 30 minutes.
- Standards: WIDA.ELD-1 (Social and Instructional Language) through school, team, library, volunteer and job emails and the register each needs; WIDA.Inform taught in full: every reply must give the specific information the sender asked for, clearly and in order, and Compose asks the student to request information. Interviews are left to interview-simulator, so the module's "interviews" wording is taught there; teacher notes say so.
- Help setting: **Lots of help**, **Some help**, **Little help** (WIDA levels 1-2, 3-4, 5-6 in teacher notes). Default Some help.
- The student plays a made-up student, "Alex Lee", at Ridgeview High School (made up). A **My info card** gives every fact to use (days free, sizes, choices), so no student ever types their own personal details. A note: "Use the info card. Don't put your real phone number or address in practice emails."
- tool.json: driver "students", minutes "20-30", modes ["Inbox", "Compose", "Phrase lab"], grades_label "Grades 9-12". Kit starter only.

## Screens and modes
Header: title "Inbox Simulator"; mode buttons **Inbox** (opens first), **Compose**, **Phrase lab**; Motion, Sound, Read. The made-up mail screen is called "Ridgeview Mail" and looks like no real email product (no logos, no brand colors).

### Inbox (opens first)
- Focus: the open email and the reply draft under it, center and the largest thing on screen, with the register meter right beside the draft so the needle moves next to the words that move it.
- Left: the message list, six threads (see Content), each with the sender's painted badge (see Art), sender, subject, a dot for unread and "Done" when the thread is resolved.
- Center: the open email, with **Hear it**. Under it, the reply box. Right: **My info card** for this thread, and the **register meter**: a horizontal bar from **Casual** to **Formal** with five steps, a shaded **Fits [name]** zone, and a needle for the current draft. The meter has words at both ends and the zone has a label, never color alone.
- Reply builder by help level:
  - Lots of help: five slots in order, **Greeting**, **Why I'm writing**, **The information**, **Ask or thank**, **Closing and name**. Each slot has three to five phrase chips at different registers (see Content), each with a small register tag (1 to 5 dots). The information slot has chips built from the info card ("I can come on Thursday.").
  - Some help: chips for Greeting and Closing; the middle three slots are text boxes with sentence starters ("I can come on ___." "Could you please ___?").
  - Little help: one text box; **Starters** shows the starters list.
- The meter moves live as chips are chosen or text is typed. A **Check** list under the meter, each a word plus ✓ or ○: **Greeting**, **Says why**, **Gives: [item 1]**, **Gives: [item 2]**, ..., **Closing**.
- **Send** is always enabled. After Send: a **What they might think** bubble (from the register) beside the sender's badge, and then the reply email arrives in the thread (from the information). A complete reply resolves the thread; a reply missing information gets a follow-up asking only for what is missing, and the student replies again.
- **Show a model reply** (after Send) shows one reply that fits, for comparison.

### Compose
- Focus: the draft with its meter beside it, as in Inbox; the task card sits above the draft.
- Three task cards, each a purpose and a recipient, with an info card: email the school counselor to ask for a meeting about choosing next year's classes; email a teacher to ask for another copy of the homework; email the pool manager to ask what to wear on the first day.
- Fields: **To** (filled), **Subject**, body (same builder by help level). Check list adds **Subject** and **Asks a clear question**. Send gives the bubble and a reply as in Inbox.

### Phrase lab
- Focus: the meter, drawn large across the middle, with the six version cards above it and the four reader buttons below.
- One message ("I can't come to practice on Friday.") in six versions on cards, from "cant make it fri sry" to "I am sorry, but I will not be able to attend practice on Friday." Drag a card onto the meter to see its register. Then pick a reader (**Friend**, **Coach**, **Teacher**, **Manager**, each a button with its badge: skateboard, whistle, beaker, life ring) and see which versions fit that reader's zone. Each card also has a **Place it** button that sets it on the meter without dragging.
- Four more message sets: saying thank you, asking for help, saying you will be late, asking for more time. Each set shows what changes from casual to formal: contractions, short forms, greetings, "please", "would" and "could".

## Content
Register scores (1 very casual to 5 very formal) for chips:
- Greetings: "Hey" 1; "Yo" 1; "Hi" 2; "Hi [first name]," 2; "Hi [title and last name]," 3; "Hello [title and last name]," 4; "Dear [title and last name]," 5.
- Why I'm writing: "about the lab" 2; "I'm writing about the lab I missed." 3; "I am writing about the lab I missed on Tuesday." 4; "Thank you for your email." 4.
- Ask or thank: "thx" 1; "Thanks!" 2; "Thank you." 3; "Thank you for your help." 4; "I appreciate your time." 5.
- Closings: "see ya" 1; "Thanks," 2; "Thank you," 3; "Best," 4; "Sincerely," 5; each followed by the name "Alex" or "Alex Lee".
- Information chips come in three registers each, for example "thurs works" 1, "I can come Thursday." 3, "I am able to come on Thursday after school." 4.

Zones: Sam (friend) 1 to 2.5; Coach Daniels 2.5 to 4; Ms. Rivera (teacher) 3 to 4.5; Ms. Patel (librarian) 3 to 4.5; Ms. Gomez (volunteer coordinator) 3 to 4.5; Mr. Okafor (pool manager, a job) 4 to 5. Compose: Mr. Haddad (counselor) 3 to 4.5; Ms. Rivera 3 to 4.5; Mr. Okafor 4 to 5.

Threads (all people, places and messages are made up):
1. Ms. Rivera, Science, "Missed lab": "Hi Alex, you missed Tuesday's lab. You can make it up after school on Wednesday or Thursday. Please tell me which day, and whether you need another copy of the lab sheet. Ms. Rivera." Info card: free Thursday; lost the lab sheet. Needed: day (Thursday); sheet (yes). Tip: "You don't have to say why you were absent. 'I was absent' is enough." Complete reply back: "Thanks, Alex. Thursday works. I'll have a new lab sheet for you." Follow-ups: "Which day works for you, Wednesday or Thursday?" / "Do you need a new lab sheet?"
2. Coach Daniels, "Practice moved": "Team, practice moves to Saturday at 9 a.m. this week. Reply to confirm you'll be there, and tell me your jersey size for the new jerseys. Coach D." Info: can come; size medium. Back: "Got it. See you Saturday. Medium is on the list." Follow-ups for each missing item.
3. Mr. Okafor, Green Street Pool, "Your application": "Dear Alex, thank you for applying to be a junior lifeguard assistant. Please reply with the days you can work in June and the name of one reference, such as a teacher or coach. Sincerely, D. Okafor, Pool Manager." Info: Mondays, Wednesdays and Fridays; reference Coach Daniels. Back: "Thank you, Alex. I have your days and will contact Coach Daniels." Follow-ups: "Which days can you work?" / "Who can we contact as a reference?"
4. Sam, "sat??": "u coming sat?? also can i borrow ur chem notes". Info: yes, coming; yes, will bring the notes. Back: "yay ok bring them sat". Follow-ups: "wait are u coming or not" / "and the notes??"
5. Ms. Patel, Library, "Overdue book": "Hello Alex, our records show that Treasure Island is two weeks overdue. Please reply to renew it for two more weeks, or tell us the day you will return it. Ms. Patel, Library." Info: you want to renew. Back: "Done. Treasure Island is renewed for two more weeks." Follow-up: "Would you like to renew it, or return it?"
6. Ms. Gomez, Riverside Park Cleanup, "Your shift": "Thanks for signing up! Please reply with your shift (8 to 10 or 10 to 12), your T-shirt size, and whether you can bring your own gloves. Ms. Gomez." Info: 10 to 12; small; no gloves. Back: "Perfect: 10 to 12, size small, and we'll have gloves for you." Follow-ups per missing item.

What they might think (register bubble), by where the meter lands; a clash is checked first. A clash (one part 2 or more steps from the mean): "[Name] thinks: 'Yo' and 'Sincerely' in one email? That's confusing." Inside the zone (ends included): "[Name] thinks: Clear and polite." Below the zone for a teacher, coach, librarian, counselor or coordinator: "[Name] thinks: A little too casual for school." Below the zone for Mr. Okafor: "Mr. Okafor thinks: This doesn't sound ready for a job yet." Above the zone for Sam: "Sam thinks: why so formal?? are you mad at me". Above the zone for anyone else: "[Name] thinks: Very polite. That's fine." (Sam's zone starts at 1 and Mr. Okafor's ends at 5, so those two never fall off the other end.)

Compose task cards: Counselor: "Ask Mr. Haddad for a meeting about choosing classes for next year. You're free Tuesday or Thursday at lunch." Needed: meeting request, the topic (classes), the times. Teacher: "Ask Ms. Rivera for another copy of Monday's homework." Needed: the request, which homework (Monday's). Manager: "Ask Mr. Okafor what to wear on your first day, June 2." Needed: the question, the day.

Phrase lab sets (six versions each, scored 1 to 5 or 6 steps): can't come Friday ("cant make it fri sry" 1, "Can't make it Friday, sorry!" 2, "Sorry, I can't come on Friday." 3, "I'm sorry, but I can't come to practice on Friday." 3.5, "I'm sorry, but I won't be able to come to practice on Friday." 4, "I am sorry, but I will not be able to attend practice on Friday." 5); thank you ("thx!!" 1 to "Thank you very much for your help with my application." 5); asking for help ("can u help w this" 1 to "Could you please help me with question 4?" 4.5); late ("gonna be late" 1 to "I will arrive about ten minutes late." 4.5); more time ("can i turn it in later" 1 to "Would it be possible to have one more day for the essay?" 5).

Typed text is scored line by line. A typed greeting line (Hey, Yo, Hi, Hello or Dear plus a name, no period) and a typed closing line (see ya, Thanks, Thank you, Best, Sincerely or Best regards, then the name) take the score of the matching chip above ("Hi" with a title and last name scores 3). Every other sentence starts at 3. Casual markers (each lowers that sentence by 1, floor 1): u, ur, r, k, kk, thx, pls, plz, gonna, wanna, gotta, lol, omg, sry, ya, yeah, nope, cuz, "??", "!!", a sentence starting with a lowercase letter, any emoji. Formal markers (each raises by 0.5, cap 5): Dear, I am writing, Thank you for, I appreciate, Would it be possible, Could you please, I would like to, Sincerely, Best regards, I am able to, I will not. A complete sentence (capital first letter, ends with . ? or !) with no casual marker and no contraction gets +0.5.

Info keywords (typed text; chips always count): Thursday ("thursday", "thurs"); sheet ("sheet" with need, another, new, copy, yes, again); confirm (be there, come, coming, yes, confirm, will attend); medium ("medium", "size m"); days (monday, wednesday and friday all three, or mon, wed, fri); reference ("daniels" or "coach"); Sam coming (coming, yes, be there, ya, yeah); notes ("notes" with bring, yes, sure, lend, ok); renew (renew, two more weeks, extend, keep it); 10 to 12 ("10-12", "10 to 12", "10 till 12", "second shift", "later shift"; a bare "10" does not count, since "8 to 10" holds it too); small ("small", "size s"); gloves ("glove" with no, not, can't, don't, do not, won't).

## Interactions in detail
- Meter value: the mean of the scores of the parts used (chips by their score, typed sentences by the marker rule). A clash is any part 2 or more steps away from the mean. The needle moves smoothly (instantly with Motion off).
- Check list: each needed item is ✓ when its chip is used or its keywords appear; Greeting ✓ for any greeting chip or a first line starting with hi, hello, hey, dear, yo; Closing ✓ for a closing chip or a last line with a closing word or the name.
- Send: the bubble comes first (from the meter), then after 1.2 seconds (no delay with Motion off) the reply (from the check list). During that wait every control stays live: opening another thread, editing or Hear it acts at once, and the reply still lands in its own thread with its unread dot. Register never blocks the information: a casual email with all the info still resolves the thread, and the bubble is the only cost.
- A thread is Done when its information is complete. The meter result is kept in the thread as "Tone: fits" or "Tone: too casual" so a student can redo it with **Write it again**.
- The tool reads only the words in its lists, and says so in **How this works**: "The meter reads only words it knows. A real reader notices more."
- Fading: after two resolved threads with the tone in the zone at the current level, the tip offers "Try with less help?" with **Yes** and **Not now**. Never automatic.
- Mode change calls `V.hush()`. Storage `inbox-simulator:v1` (try/catch): thread progress, drafts, help setting; **Clear** asks first. Sound starts on, as the kit sets it.
- Sizes: at 1366x768 the list, the open email, the builder, the meter and Send fit; at 1000x625 the list collapses to a **Messages** button; at 760 the info card and meter move above the builder; at 375 one column: email, meter, builder, Send pinned at the bottom. No horizontal scroll.

## Look
- Own light `:root`, a calm mail screen: `--paper #f3f5f8`, `--panel #ffffff`, `--ink #1b2430`, `--muted #556070`, `--line #d9dee6`, accent `--brand #8c1c13` (brick red: Send, unread dots, active mode), `--btn #8c1c13`, `--head-ink #ffffff`, `--focus #1d4ed8`. Meter ends: Casual `#8a5a00`, Formal `#2b4a8a`, the zone a light band with a dark outline and its label.
- Neighbors: interview-simulator brick coral #b4472b (dE about 15); editors-in-the-margin #b3261e (dE 14.2); classroom-phrases-game teal.
- The painted badges are bright everyday objects on a soft round cream ground, each in a 40 px circle in the list and 64 px beside the open email; the badge is never the only cue (the name is always beside it).
- Contrast: ink on paper 14.33:1; muted on paper 5.84:1, on panel 6.38:1; brand on paper 8.39:1; white on brand 9.17:1; Casual label 5.43:1, Formal label 7.85:1 on paper; focus on panel 6.70:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`), one style for all seven: "<object>, a single everyday object, bright flat colors, soft gouache illustration, centered, plain white background". Each sender is shown by an object, not a face, so no image has a person. Each: 1:1; cutout yes; people no; clipped to a circle as the sender's badge in the message list, beside the open email and in the bubble.
- badge-rivera: "A clear glass lab beaker half full of green liquid"; Ms. Rivera (science); also the Teacher reader in Phrase lab.
- badge-coach: "A silver sports whistle on a red lanyard"; Coach Daniels; also the Coach reader.
- badge-pool: "A red and white life ring buoy with a coiled white rope"; Mr. Okafor (pool); also the Manager reader.
- badge-sam: "A blue skateboard with yellow wheels, seen from above at an angle"; Sam; also the Friend reader.
- badge-library: "A small stack of three hardcover books with plain colored covers"; Ms. Patel (library).
- badge-cleanup: "A pair of green garden work gloves beside a fallen orange maple leaf"; Ms. Gomez (park cleanup).
- badge-counselor: "A wooden desk organizer holding pencils and a small blank desk calendar"; Mr. Haddad (counselor, Compose).

7 images, none with people. Drawn in code: the mail screen, message list, email text, meter, chips, check list and bubbles (controls and text that change with every draft).

## Voice
Bank voice `easy-coach` (Umbriel), style "Say in an easy-going, encouraging way, like a relaxed coach helping with emails." Not used by any other tool in this group or its neighbors. `Curio.voice`, `scope: () => state.mode`. Emails are read on Hear it (recorded).
- how, w-inbox (Inbox welcome; stale when a thread is opened): "Tap an email to open it. Check your info card, build a reply, then press Send."
- how, meter (first time the needle moves; stale on Send): "Watch the meter. The shaded zone is what fits this person."
- event, missing (a follow-up arrives; stale when the thread is answered or another thread opens): "They wrote back. Add what they asked for, then press Send again."
- event, resolved (a thread is complete; stale when another thread opens): "Done. You gave them everything they asked for."
- event, too-casual (bubble below the zone; stale on the next edit or Send): "That's a bit casual for this reader."
- event, too-formal (Sam's bubble above the zone; stale the same way): "That's very formal for a friend."
- event, clash (clash bubble; stale the same way): "Some parts are casual and some are formal. Pick one style."
- how, less-help (the fading offer; stale when Yes or Not now is tapped): "That fit well. Tap Yes to try with less help, or Not now."
- how, w-compose (Compose welcome; stale when a task card is tapped): "Tap a task card. Write a subject, then ask your question clearly and press Send."
- how, w-lab (Phrase lab welcome; stale when a card is placed): "Drag a version onto the meter, or tap Place it. Then tap a reader to see which ones fit."
- event, every email text (on Hear it; stale when another email opens).

## Family engine
None.

## Sources
- WIDA ELD Standards Framework, 2020 Edition (Social and Instructional Language; Inform): https://wida.wisc.edu/teach/standards/eld.
- Register and email conventions (greetings, closings, contractions in formal writing): Purdue Online Writing Lab, "Email Etiquette," https://owl.purdue.edu/owl/general_writing/academic_writing/email_etiquette.html (confirm the page at build). The register scores are the tool's own judgments, stated on screen.
- Treasure Island (Robert Louis Stevenson, 1883) is named only as a book title.
- All people, schools, the pool, the park cleanup and every email are made up for Curio Class.
- Checks run (Python, 2026-10-29, on the meter rules above). The draft rule scored every plain typed sentence 3 and typed greetings and closings as plain sentences, so a fully formal typed job reply ("Dear Mr. Okafor," two plain sentences, "Sincerely, Alex Lee") came to 3.25, below Mr. Okafor's zone of 4 to 5: the job thread could never be in tone at Little help. With greeting and closing lines scored as chips and the +0.5 for complete sentences, it comes to 4.25 (4.125 with contractions), in the zone. Other results: "can u help pls" 1; "Could you please help me?" 4; Ms. Rivera typed reply (Hi Ms. Rivera, two sentences, Thank you) 3.25, in her zone; Sam "Dear Sam, I am writing to confirm..." 4.375, too formal; Sam "ya coming, ill bring the notes" 1, in zone; a casual Sam reply (hey / yeah im coming sat / ill bring the notes / see ya) 1.25, in zone; a Coach reply with contractions 2.625, in zone; "Hey Mr. Okafor," with "Sincerely" mean 3.17 with a clash (Hey is 2.17 below). The bubble table had no line for a reply above a teacher's zone; it now has one. The "10" keyword for the cleanup shift also ticked "8 to 10", so a bare 10 no longer counts.
- Phrase lab scores are the authored chip scores listed above (not the typed rule): Friend zone 1 to 2.5 holds the versions scored 1 and 2; Coach 2.5 to 4 holds 3, 3.5 and 4; Manager 4 to 5 holds 4 and 5.

## Done when
- Ms. Rivera's thread: a reply with "Hi Ms. Rivera,", "I can come Thursday.", "Yes, I need another lab sheet.", "Thank you," lands in the zone and resolves; dropping the sheet line gets only the sheet follow-up.
- Sam's thread: "Dear Sam, I am writing to confirm..." with all info resolves the thread and shows the too-formal bubble; "ya coming, ill bring the notes" resolves in the zone.
- Mr. Okafor: a reply naming only Monday and Friday gets the days follow-up; "Hey" plus "Sincerely" shows the clash bubble.
- Ms. Gomez: "10 to 12, small, I can't bring gloves" resolves; "I have gloves" does not tick gloves.
- Typed "can u help pls" scores 1 on the meter; "Could you please help me?" scores 4; at Little help "Dear Mr. Okafor, / I can work Mondays, Wednesdays and Fridays. / My reference is Coach Daniels. / Sincerely, Alex Lee" lands in Mr. Okafor's zone and resolves the thread.
- Phrase lab: the six Friday versions sit in score order; Friend (zone 1 to 2.5) shows the versions scored 1 and 2 in the zone; Manager (4 to 5) shows the versions scored 4 and 5.
- No email field ever asks for the student's own details; the info card holds every fact.
- Focus: at 1366x768 and 1000x625 the open email, the draft and the meter beside it are the largest thing on screen; in Phrase lab the meter is.
- Tap while it plays: during the 1.2 s wait after Send or an email reading, opening another thread, typing or Hear it acts at once, and the reply still lands in its own thread.
- Storage survives reload; Clear asks first.
- How lines are spoken once in five actions; event lines repeat; no line names a disabled control.
- No horizontal scroll at any listed size; Send stays reachable at 375.

## Open questions
- None beyond the group's home-language question (see then-what-happened).
