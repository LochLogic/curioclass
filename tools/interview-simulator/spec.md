# Interview Simulator

## One idea
Sit across the desk from a hiring manager and build each answer from your own experiences, while the manager's notepad, in plain view, writes down only what was specific (what happened, what you did, how it turned out) and leaves a "?" for everything vague, so you learn that an interview is remembered as the notes someone took, and a vague answer leaves a blank page.

## Not like
- workplace-scenarios (CTE 6-8, specced): choices once you have the job, rippling across a day. Here getting the job, one question at a time, and nothing ripples.
- conflict-coach (SEL 6-8, built): rewinds one argument to watch a face react. Here no faces or feelings meter; the feedback is a written notepad.
- startup-booth (9-12, this group): pitching to an investor with business numbers. Here talking about yourself, with stories.
- hospital-shift, path-planner (9-12, careers, this group): what jobs are and how to train for them. Here how to show you're ready for one.
- the-credit-card-diaries (9-12, this group): a story told to you. Here you tell the story.

## Who and how
- Grade 9-12, career and technical education, module "Resumes and Interviews".
- Topic line: job interviews and resume lines
- Driver: students on laptops, alone or in pairs (one reads the questions aloud, one answers); the teacher can project Hiring seat for a class discussion. 20 to 40 minutes.
- Standards: CTE.Career Ready Practices (communicate clearly and effectively; plan education and career paths; act as a responsible employee).

## Screens and modes
Header: title, topic line, modes (`.seg`): `Interview` (default), `Hiring seat`, `Resume lines`; then `Read`, `Motion`, `Sound`.

**Interview.**
1. Setup screen. Focus: the three posting cards, side by side. Each card has its storefront picture (Art) over the posting text (Content); tap one, then pick 4 of 10 experience cards, each with its painted object (Art): "Pick the four that are most like you, or that you'd like to talk about." `Start interview` (enabled once a posting and four experiences are picked).
2. Interview screen. Focus: the manager's notepad, the largest thing on the stage, lying on the desk facing you, with the question card above it. Stage: a painted office seen from the candidate's chair (Art): the manager's empty chair, a window and a shelf behind, and the desk across the front with a coffee mug and a blank name plate (the manager's name, Ms. Rivera at Pawpath, Mr. Chen at Starlite, Ms. Brooks at Brightside, written in code on the plate). The manager is never drawn: a voice, a name plate and a mug. The question appears in a speech card ("Tell me about a time you worked on a team.") and is spoken.
   - Answer builder in the panel: 6 to 8 sentence chips for this question (Content), drawn from your four experiences and from general lines. Tap chips to add them to "Your answer" (up to 4); drag to reorder, or use the up and down buttons on each; the x button removes.
   - `Say it` (enabled once the answer has a chip) delivers the answer: the chips play as a short speech bubble from your side, and the notepad writes one line per chip in the manager's shorthand ("Food bank: noticed cans mixed with dry goods (S). Made a sort chart (A). Line moved 2x faster (R)."), with "?" for a vague chip, and a margin flag for a chip that hurts ("blamed teammates"). Lines write in over about 2 seconds (instant with Motion off).
   - Under the notepad, a checklist for this answer: Situation, Action, Result, Specific, Positive, Short enough (4 chips or fewer). Ticks are words plus icons.
   - `Try that answer again` clears this answer (the notepad strikes its old lines through, so the history stays honest). `Next question` moves on.
   - `Say it your way` (optional): a text box to type your own answer for this question; kept in memory only, never saved. The tool does not grade it; it shows the same checklist as self-check boxes for you to tick.
3. After 7 questions: the closing screen. The manager says "Thanks for coming in. We'll be in touch by Friday." The full notepad is shown as the manager left it, with a summary box "What I'd remember" (the lines with S, A or R) and "What I couldn't write down" (the "?" lines). Tips card: send a short thank-you note within a day. `New interview` (back to setup).

**Hiring seat.** Focus: the candidate's answer card, centered, with your notepad beside it. You are the manager: the stage is the same office painted from the manager's side (an empty candidate's chair across the desk). One question, three made-up candidates' answers (text, also voiced). Tap the phrases worth writing down (each answer's phrases are buttons); they copy onto your notepad. Then `Compare with the manager`: your notes beside the manager's, with phrases you both chose highlighted and a one-line why for each the manager noted. Five questions, `Next question`.

**Resume lines.** Focus: the resume mockup with the bullet being built, centered. Turn an experience into a resume bullet. Pick one of your four experiences (or any of the ten); build the line from three trays: an action verb (Organized, Trained, Built, Led, Fixed, Sorted, Taught, Raised, Scheduled, Served), what you did (two to three choices per experience), and a result with a number (two choices per experience, one with a number). The finished bullet shows in a resume mockup (drawn in code) with the right format ("Organized a sorting system for 400 donated cans a week, cutting sorting time in half"). The line is flagged if it has no number ("Try a result with a number") or starts with "Responsible for" (available as a tray choice so students see the difference). `Copy all lines` copies the student's built bullets to the clipboard of this device (nothing saved).

## Content
**Postings** (made up):
- Pawpath Pet Supply, part-time store associate. "Help customers find what their pets need, stock shelves, keep the store clean. Weekends required. We just started free Saturday adoption days with the county shelter."
- Starlite Cinema, crew member. "Sell tickets and snacks, clean theaters between shows, help guests find seats. Evenings and weekends. Busy summer blockbuster season."
- Brightside Learning Center, homework helper. "Help students in grades 2 to 5 with reading and math after school. Patient, organized, on time. We're adding a summer reading club."

**Experiences** (each has S, T, A and R chips; the R always has a number or a concrete change):
1. Babysat my two younger cousins every Saturday for a year. 2. JV soccer team. 3. Volunteered at a food bank sorting donations. 4. Science fair team of four. 5. Mowed lawns for five neighbors as my own small business. 6. Stage crew for the school play. 7. Ran the bake sale table for a club fundraiser. 8. Took care of our family's two dogs. 9. Tutored a classmate in algebra. 10. Worked the concession stand at home games.
Example chips for 3 (food bank): S "At the food bank, canned goods and dry goods kept getting mixed up." T "Our shift lead asked me to speed up sorting." A "I made a color-coded chart and set up two bins per table." R "Our table sorted about twice as many boxes that shift." The builder writes all 40 experience chips in this pattern.

**Questions and general chips** (traps marked):
1. "Tell me about yourself." Good: "I'm a junior at (school) who likes (experience topic)." "I've done (experience) for (length)." "I'm looking for weekend work where I can (posting task)." Traps: "Well, I was born in..." (off topic), "I don't know, I'm pretty normal." (vague).
2. "Why do you want to work here?" Good: chips that quote the posting's own detail ("I saw you started Saturday adoption days..."). Traps: "I just need money." (honest but thin; the notepad writes "?"), "My friend works here." (vague).
3. "Tell me about a time you worked on a team." Experience S, T, A, R chips. Trap: "My last group was lazy, so I did everything." (blames others).
4. "Tell me about a time something went wrong. What did you do?" Experience chips with a problem. Trap: "Nothing really goes wrong for me." (avoids the question).
5. "What would you do if a customer (guest, parent) was upset?" Good: "Listen first, without interrupting." "Repeat back what they need." "Fix what I can, and get a manager for what I can't." Trap: "Tell them it's not my fault."
6. "What's your availability?" Good: exact days and hours matching the posting. Traps: "Whenever." (vague), "Not weekends." (conflicts with the posting: margin flag "posting says weekends").
7. "Do you have any questions for us?" Good: "What does a great first month look like here?" "Who would I be working with?" Traps: "No." "How soon can I take vacation?" (fine to ask later; flagged "save for the offer").

**Hiring seat**: five questions, three candidate answers each (made up; one specific, one vague, one mixed), written by the builder to the same S/A/R tags.

## Interactions in detail
- Every chip has tags: S, T, A, R, specific, vague, negative, off-topic, posting-detail, conflict. The notepad writes: one shorthand line per S, T, A or R chip; "?" for a vague or off-topic chip; a margin flag for negative or conflict chips; "researched us" for a posting-detail chip.
- Checklist: Situation ticks with any S chip, Action with any A, Result with any R; Specific when there is no vague chip; Positive when there is no negative chip; Short enough at 4 chips or fewer (the builder holds 4 at most, so a fifth tap says "Four is plenty. Remove one to add another."). Questions 1, 2, 5, 6 and 7 tick only Specific, Positive and Short (S, A, R are dimmed with "not needed for this question").
- Chip order: STAR order (S before A before R) adds "Clear order" to the notepad's margin; other orders are allowed with no penalty beyond the missing note.
- An empty answer: `Say it` is disabled with "Add at least one chip."
- The notepad's 2-second write never blocks: a tap on Next question, Try that answer again or a chip during it finishes the writing at once and then acts; the speech bubble and its line stop.
- No hire verdict and no score: the manager's closing line is the same every time; the notepad is the result.
- Nothing typed is stored or sent. `Say it your way` text is cleared on `New interview` and on page close.
- Tab order: chips, the answer list, Say it, Next question, then the notepad. Drag has the up and down button path.
- Sizes: the office and notepad are laid out at real pixels (the office picture is cropped to fit, the desk cutout always along the bottom); below 760 px the notepad sits above the panel; at 680x425 the stage shows only the notepad and the question card over the desk; at 375 the chips wrap in a scroll tray with Say it pinned.

## Look
- Own light `:root` (a bright office): `--paper #f6f4f1`, `--panel #ffffff`, `--ink #1f2328`, `--muted #5b6168`, `--line #e2ded8`, `--btn #b4472b`, `--head-ink #ffffff`, `--focus #1d4ed8`. Accent `--brand #b4472b` (brick coral: Say it, the active mode, chip borders on hover).
- Notepad: legal-pad yellow `#fff6c7` with blue rules `#9cc3e6` and a red margin line `#d9534f`; handwriting-style text in `#1f2a44` (system font in italics, not a script font, for readability); "?" marks in `#8a5a00`; margin flags `#a3241a` with a flag icon and a word.
- The office paintings are warm daylight with soft wood and plant greens, kept a little muted behind the bright notepad.
- Contrast: accent on paper 4.93:1, on panel 5.42:1; white on accent 5.42:1; ink on paper 14.39:1; muted on panel 6.26:1 (on paper 5.7:1); notepad ink on yellow 13.08:1; "?" brown 5.44:1; flag red 6.82:1 on yellow; name-plate text `#1f2328` on the painted brass plate checked by the builder at 7:1 or more (the plate is painted plain light brass).
- Differs from workplace-scenarios (lake blue camp daylight), career-match-quiz (cream, navy, coral #e46c4b on cream is lighter and pinker), and this batch's journal raspberry and trail-map green, its other light tools.

## Art
Local FLUX (`scripts/localart.py`), one session, no people. Shared style line: "warm realistic digital painting, soft daylight, tidy small business office". Blank surfaces on the name plate, signs and screens. Webp.
- iv-office: "a small tidy office seen from the visitor's chair, an empty office chair behind a wooden desk, a window with daylight and a plant, a shelf of binders, (style)"; 16:9; cutout no; people no; the Interview stage background.
- iv-desk: "the near edge of a wooden office desk seen from the front, a white coffee mug and a plain light brass name plate on it, plain white background, (style)"; 4:1; cutout yes; people no; laid along the bottom of the Interview stage, the notepad drawn on it, the name in code on the plate.
- iv-office-back: "the same small office seen from behind the desk, an empty visitor's chair across the desk, an office door and a coat hook, (style)"; 16:9; cutout no; people no; the Hiring seat stage.
- Storefronts (4:3; cutout no; people no; on the posting cards, 480 px wide; signs blank, the store name in code on a band under the picture):
  - iv-pet: "the front of a small pet supply store with a blank sign, bags of pet food and a dog bed in the window, (style)".
  - iv-cinema: "the front of a small old movie theater at dusk with a blank marquee and warm lights, (style)".
  - iv-learning: "the front of a small after-school learning center with a blank sign, colorful book posters with no words and a reading corner seen through the window, (style)".
- Experience objects (a kit of ten; 1:1; cutout yes; people no; 160 px on the experience cards and in the Resume lines tray): one shared prompt "a single (object) centered on a plain white background, (style)", for these objects: a picture book and a stack of toy blocks; a soccer ball on grass; a cardboard box of canned food; a blank science fair tri-fold board; a push lawn mower; a stage spotlight on a stand; a tray of cookies and cupcakes; two dog leashes and a dog bowl; an open notebook with algebra scribbles and a pencil; a red and white striped box of popcorn. Sizing rule: each object fills 75% of its square, centered.
- 16 images, none with people. Drawn in code: the notepad, the question card and speech bubble, chips, checklist, resume mockup and every label.

## Voice
Bank voice `friendly-dad` (Achird), "Say in a relaxed, friendly way, like a kind dad helping with homework": a relaxed, kind store manager reading the questions. Not used by another tool `neighbors.py` lists or by this batch. `Curio.voice`, `scope: () => state.mode`. The questions are voiced because an interview is spoken; chips and notes are on screen only.
- welcomeInterview (how; on the setup screen; stale when a posting is tapped): "Tap a job posting, then tap four experiences that sound like you."
- startHow (how; once four are picked; stale when Start interview is tapped): "Tap Start interview when you're ready."
- buildHow (how; at the first question; stale when Say it is tapped): "Tap chips to build your answer, then tap Say it. Watch my notepad."
- q1 to q7 (event; as each question appears; stale on Next question): the question text, with the posting's word for customer.
- noteVague (event; after Say it when any "?" was written; stale on the next Say it): "I wasn't sure what to write for part of that."
- noteGood (event; after Say it with S, A and R; stale on the next Say it): "That one was easy to write down."
- nextHow (how; after the first Say it; stale when Next question or Try that answer again is tapped): "Tap Next question, or Try that answer again."
- closing (event; after question 7; stale when New interview is tapped): "Thanks for coming in. We'll be in touch by Friday."
- welcomeHiring (how; on entering Hiring seat; stale when a phrase is tapped): "Now you're the manager. Tap the phrases worth writing down, then tap Compare with the manager."
- candidate answers (event; read when each candidate's turn comes; stale on Next question): the builder's 15 answers, each under 200 characters.
- welcomeResume (how; on entering Resume lines; stale when a tray choice is tapped): "Tap a verb, what you did and a result with a number."

## Family engine
none.

## Sources
- The STAR method (Situation, Task, Action, Result) for behavioral questions: CareerOneStop (U.S. Department of Labor), "Interview Tips" and "Prepare for behavioral questions" (https://www.careeronestop.org/JobSearch/Interview/interview-tips.aspx).
- Common interview questions, preparing questions to ask, and thank-you notes: CareerOneStop, "Interview" section (https://www.careeronestop.org/JobSearch/Interview/interview.aspx).
- Resume bullets with action verbs and results: CareerOneStop, "Resumes and Applications" (https://www.careeronestop.org/JobSearch/Resumes/resume-tips.aspx).
- Career Ready Practices: Advance CTE, Career Ready Practices (https://careertech.org/resource/career-ready-practices/).
- Postings, experiences, chips, candidates and the managers: made up for this tool.
- Checks run: no numeric rules beyond the chip count. Walked the checklist rule by hand on the worked answers: food bank S, A, R in order ticks all six and adds "Clear order"; "I just need money." alone ticks Positive and Short but not Specific; four chips is the cap, so Short enough can never fail inside the builder (it stays as a visible tick that teaches the limit).

## Done when
1. Picking 4 experiences fills questions 3 and 4 only with chips from those experiences plus the general chips.
2. A food bank answer S, A, R in order writes three notepad lines plus "Clear order", ticks Situation, Action, Result, Specific, Positive, Short.
3. "I just need money." writes "?"; "My last group was lazy..." writes a margin flag; "Not weekends." on a weekend posting flags the conflict.
4. A fifth chip is refused with the four-chip message; an empty answer cannot be said.
5. Try that answer again strikes old notepad lines rather than erasing them.
6. Hiring seat compares the student's tapped phrases with the manager's for all five questions.
7. Resume lines flags a bullet without a number and one starting "Responsible for"; Copy all lines copies the built bullets.
8. Nothing typed survives New interview or a reload (localStorage holds nothing from this tool).
9. Focus: at 1366x768 and 680x425 the notepad is the largest thing on the Interview stage; the answer card in Hiring seat and the mockup in Resume lines are central.
10. Tap while it plays: Next question tapped while the notepad writes finishes the notes at once and shows the next question, with no stale line after.
11. All 16 paintings load with no person or fake lettering; the manager's name reads on the plate at every size.
12. Question card, chips and Say it are visible without scrolling at every STANDARDS.md size; how lines once each in five actions in a row; questions, noteVague, noteGood and closing every time, dropped when stale.

## Open questions
- The module is "Resumes and Interviews". This spec adds a small Resume lines mode (bullets only, no full resume). Enough, or should resumes get their own tool later?
- Students may pick experiences like their own, but nothing about them is typed except in the optional, unsaved Say it your way box. OK as is?
