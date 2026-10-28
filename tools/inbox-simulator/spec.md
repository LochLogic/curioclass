# Inbox Simulator

## One idea
Every email has two readers' reactions you can see: a register meter shows how formal your reply sounds against the zone that fits this person (a friend, a coach, a teacher, a job), and the person's next email shows whether you gave them the information they asked for, so a perfectly polite reply that forgets the day you can work still gets "Which days can you work?" back, and a perfect answer to a friend written like a cover letter gets "why so formal?? are you mad at me".

## Not like
- interview-simulator (cte 9-12, specced): answering a hiring manager's spoken questions with specific stories. Here written email only, about schedules, requests and replies; no interviews (overlap note).
- classroom-phrases-game (eld K-2, built): sixteen spoken classroom phrases. Here written messages, register and requested information at high school level.
- workplace-scenarios (cte 6-8, specced): choices at work that ripple through a day. Here each choice is a word or phrase and the result is the reader's reply.
- audience-shift-briefing (ela 9): one finding presented to three rooms. Here many short messages, each to one reader, and register is measured phrase by phrase.
- argument-frames-pro, historian-s-toolkit, chart-narrator, definition-duel (eld 9-12, this group): academic language. This is the group's social and instructional language tool.

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
- Left: the message list, six threads (see Content), each with sender, subject, a dot for unread and "Done" when the thread is resolved.
- Center: the open email, with **Hear it**. Under it, the reply box. Right: **My info card** for this thread, and the **register meter**: a horizontal bar from **Casual** to **Formal** with five steps, a shaded **Fits [name]** zone, and a needle for the current draft. The meter has words at both ends and the zone has a label, never color alone.
- Reply builder by help level:
  - Lots of help: five slots in order, **Greeting**, **Why I'm writing**, **The information**, **Ask or thank**, **Closing and name**. Each slot has three to five phrase chips at different registers (see Content), each with a small register tag (1 to 5 dots). The information slot has chips built from the info card ("I can come on Thursday.").
  - Some help: chips for Greeting and Closing; the middle three slots are text boxes with sentence starters ("I can come on ___." "Could you please ___?").
  - Little help: one text box; **Starters** shows the starters list.
- The meter moves live as chips are chosen or text is typed. A **Check** list under the meter, each a word plus ✓ or ○: **Greeting**, **Says why**, **Gives: [item 1]**, **Gives: [item 2]**, ..., **Closing**.
- **Send** is always allowed. After Send: a **What they might think** bubble (from the register) and then the reply email arrives in the thread (from the information). A complete reply resolves the thread; a reply missing information gets a follow-up asking only for what is missing, and the student replies again.
- **Show a model reply** (after Send) shows one reply that fits, for comparison.

### Compose
- Three task cards, each a purpose and a recipient, with an info card: email the school counselor to ask for a meeting about choosing next year's classes; email a teacher to ask for another copy of the homework; email the pool manager to ask what to wear on the first day.
- Fields: **To** (filled), **Subject**, body (same builder by help level). Check list adds **Subject** and **Asks a clear question**. Send gives the bubble and a reply as in Inbox.

### Phrase lab
- One message ("I can't come to practice on Friday.") in six versions on cards, from "cant make it fri sry" to "I am sorry, but I will not be able to attend practice on Friday." Drag a card onto the meter to see its register. Then pick a reader (**Friend**, **Coach**, **Teacher**, **Manager**) and see which versions fit that reader's zone.
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

What they might think (register bubble), by where the meter lands: inside the zone, "[Name] thinks: Clear and polite." Too casual for a teacher, coach, librarian or coordinator: "[Name] thinks: A little too casual for school." Too casual for Mr. Okafor: "Mr. Okafor thinks: This doesn't sound ready for a job yet." Too formal for Sam: "Sam thinks: why so formal?? are you mad at me". Slightly formal for Coach: "Coach thinks: Very polite. That's fine." A clash (one part 2 or more steps from the rest): "[Name] thinks: 'Yo' and 'Sincerely' in one email? That's confusing."

Compose task cards: Counselor: "Ask Mr. Haddad for a meeting about choosing classes for next year. You're free Tuesday or Thursday at lunch." Needed: meeting request, the topic (classes), the times. Teacher: "Ask Ms. Rivera for another copy of Monday's homework." Needed: the request, which homework (Monday's). Manager: "Ask Mr. Okafor what to wear on your first day, June 2." Needed: the question, the day.

Phrase lab sets (six versions each, scored 1 to 5 or 6 steps): can't come Friday ("cant make it fri sry" 1, "Can't make it Friday, sorry!" 2, "Sorry, I can't come on Friday." 3, "I'm sorry, but I can't come to practice on Friday." 3.5, "I'm sorry, but I won't be able to come to practice on Friday." 4, "I am sorry, but I will not be able to attend practice on Friday." 5); thank you ("thx!!" 1 to "Thank you very much for your help with my application." 5); asking for help ("can u help w this" 1 to "Could you please help me with question 4?" 4.5); late ("gonna be late" 1 to "I will arrive about ten minutes late." 4.5); more time ("can i turn it in later" 1 to "Would it be possible to have one more day for the essay?" 5).

Casual markers for typed text (each lowers that sentence by 1, floor 1): u, ur, r, k, kk, thx, pls, plz, gonna, wanna, gotta, lol, omg, sry, ya, yeah, nope, cuz, "??", "!!", a greeting of Hey or Yo, a sentence starting with a lowercase letter, any emoji. Formal markers (each raises by 0.5, cap 5): Dear, I am writing, Thank you for, I appreciate, Would it be possible, Could you please, I would like to, Sincerely, Best regards, I am able to, I will not. A plain typed sentence starts at 3.

Info keywords (typed text; chips always count): Thursday ("thursday", "thurs"); sheet ("sheet" with need, another, new, copy, yes, again); confirm (be there, come, coming, yes, confirm, will attend); medium ("medium", "size m"); days (monday, wednesday and friday all three, or mon, wed, fri); reference ("daniels" or "coach"); Sam coming (coming, yes, be there, ya, yeah); notes ("notes" with bring, yes, sure, lend, ok); renew (renew, two more weeks, extend, keep it); 10 to 12 ("10", "10-12", "10 to 12", "second shift"); small ("small", "size s"); gloves ("glove" with no, not, can't, don't, do not, won't).

## Interactions in detail
- Meter value: the mean of the scores of the parts used (chips by their score, typed sentences by the marker rule). A clash is any part 2 or more steps away from the mean. The needle moves smoothly (instantly with Motion off).
- Check list: each needed item is ✓ when its chip is used or its keywords appear; Greeting ✓ for any greeting chip or a first line starting with hi, hello, hey, dear, yo; Closing ✓ for a closing chip or a last line with a closing word or the name.
- Send: the bubble comes first (from the meter), then after 1.2 seconds (no delay with Motion off) the reply (from the check list). Register never blocks the information: a casual email with all the info still resolves the thread, and the bubble is the only cost.
- A thread is Done when its information is complete. The meter result is kept in the thread as "Tone: fits" or "Tone: too casual" so a student can redo it with **Write it again**.
- The tool reads only the words in its lists, and says so in **How this works**: "The meter reads only words it knows. A real reader notices more."
- Fading: after two resolved threads with the tone in the zone at the current level, the tip offers "Try with less help?" with **Yes** and **Not now**. Never automatic.
- Mode change calls `V.hush()`. Storage `inbox-simulator:v1` (try/catch): thread progress, drafts, help setting; **Clear** asks first.
- Sizes: at 1366x768 the list, the open email, the builder, the meter and Send fit; at 1000x625 the list collapses to a **Messages** button; at 760 the info card and meter move above the builder; at 375 one column: email, meter, builder, Send pinned at the bottom. No horizontal scroll.

## Look
- Own light `:root`, a calm mail screen: `--paper #f3f5f8`, `--panel #ffffff`, `--ink #1b2430`, `--muted #556070`, `--line #d9dee6`, accent `--brand #8c1c13` (brick red: Send, unread dots, active mode), `--btn #8c1c13`, `--head-ink #ffffff`, `--focus #1d4ed8`. Meter ends: Casual `#8a5a00`, Formal `#2b4a8a`, the zone a light band with a dark outline and its label.
- Neighbors: interview-simulator brick coral #b4472b (dE about 15); editors-in-the-margin #b3261e (dE 14.2); classroom-phrases-game teal.
- Contrast: ink on paper 14.33:1; muted on paper 5.84:1, on panel 6.38:1; brand on paper 8.39:1; white on brand 9.17:1; Casual label 5.43:1, Formal label 7.85:1 on paper; focus on panel 6.70:1. All pass AA.

## Art
None: drawn in code (mail list, envelopes, meter, avatars as initials in circles). No people.

## Voice
Bank voice `easy-coach` (Umbriel), style "Say in an easy-going, encouraging way, like a relaxed coach helping with emails." Not used by any other wave 4 tool or ELD tool. `Curio.voice`, `scope: () => state.mode`. Emails are read on Hear it (recorded).
- w-inbox (how): "Open an email. Check your info card, build a reply, then press Send."
- meter (how, first time the needle moves): "Watch the meter. The shaded zone is what fits this person."
- missing (event, a follow-up arrives; stale when answered): "They wrote back. Something they asked for is missing."
- resolved (event): "Done. You gave them everything they asked for."
- too-casual (event): "That's a bit casual for this reader."
- too-formal (event): "That's very formal for a friend."
- clash (event): "Some parts are casual and some are formal. Pick one style."
- less-help (how): "That fit well. Want to try with less help?"
- w-compose (how): "Pick a task. Write a subject, then ask your question clearly."
- w-lab (how): "Drag a version onto the meter. Then pick a reader and see which ones fit."
- every email text (event, on Hear it).

## Family engine
None.

## Sources
- WIDA ELD Standards Framework, 2020 Edition (Social and Instructional Language; Inform): https://wida.wisc.edu/teach/standards/eld.
- Register and email conventions (greetings, closings, contractions in formal writing): Purdue Online Writing Lab, "Email Etiquette," https://owl.purdue.edu/owl/general_writing/academic_writing/email_etiquette.html (confirm the page at build). The register scores are the tool's own judgments, stated on screen.
- Treasure Island (Robert Louis Stevenson, 1883) is named only as a book title.
- All people, schools, the pool, the park cleanup and every email are made up for Curio Class.

## Done when
- Ms. Rivera's thread: a reply with "Hi Ms. Rivera,", "I can come Thursday.", "Yes, I need another lab sheet.", "Thank you," lands in the zone and resolves; dropping the sheet line gets only the sheet follow-up.
- Sam's thread: "Dear Sam, I am writing to confirm..." with all info resolves the thread and shows the too-formal bubble; "ya coming, ill bring the notes" resolves in the zone.
- Mr. Okafor: a reply naming only Monday and Friday gets the days follow-up; "Hey" plus "Sincerely" shows the clash bubble.
- Ms. Gomez: "10 to 12, small, I can't bring gloves" resolves; "I have gloves" does not tick gloves.
- Typed "can u help pls" scores 1 on the meter; "Could you please help me?" scores 3.5.
- Phrase lab: the six Friday versions sit in score order; Friend (zone 1 to 2.5) shows the versions scored 1 and 2 in the zone; Manager (4 to 5) shows the versions scored 4 and 5.
- No email field ever asks for the student's own details; the info card holds every fact.
- Storage survives reload; Clear asks first.
- How lines are spoken once in five actions; event lines repeat.
- No horizontal scroll at any listed size; Send stays reachable at 375.

## Open questions
- None beyond the group's home-language question (see then-what-happened).
