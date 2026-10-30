# Growing Up Q&A

## One idea
A shelf of the questions kids really ask about growing up, each answered in a few calm sentences, beside an age ribbon that draws every change as a wide band of ages, not a birthday, so "Am I normal?" gets its honest answer: normal is a range, and every body runs on its own clock.

## Not like
- body-systems-tour (3-5 health, explorer, same group): how body systems work minute to minute. Growing Up Q&A is how a body changes over years; no organs or rides.
- label-detective (3-5 health, mystery): cases and proof. Nothing here is a case or a quiz; it is read-and-browse.
- germ-spread-sim (3-5 health, simulator): a running simulation. Here nothing runs; the only moving part is an age slider.
- mind-map (9-12 health, explorer, built): mental health conditions for teens with crisis lines. This is puberty basics for ages 8 to 11, with trusted adults and the school nurse as the help, no crisis content.
- Concept change: the concept's anonymous question box is replaced (Open questions): no text box at all. The shelf of real-kid questions, the teacher's paper question box and the "Who can I ask?" mode carry the same purpose with nothing typed, stored or sent.

## Who and how
- Grade 3-5 (usually used in grades 4 and 5), Health, module Growing Up (puberty basics and changes).
- Driver: either. Students on their own laptops (headphones suggested), or a teacher on a projector choosing which cards to open.
- Minutes: 10-30.
- Standards: NHES.S1 (core concepts: growth and development), NHES.S3 (access valid health information and trusted adults).
- Topic line: "puberty and body changes".
- Modes (tool.json): ["Questions", "Age ribbon", "Who can I ask?"]. Explore only: no score, no quiz.

## Screens and modes
Header: title "Growing Up Q&A" with small line "Puberty and body changes", mode buttons **💬 Questions**, **📏 Age ribbon**, **🤝 Who can I ask?** (keys 1 to 3), **Motion**, **Sound**, **Read**, and a small text button **For teachers** at the far right.

A line under the header on every mode, small and calm: "Every body changes on its own schedule. If you have a question, ask a trusted adult."

### Questions (opens first)
- Top: topic chips that filter the shelf: **All**, **🌱 Changes for everyone**, **🌸 Girls' bodies**, **🌊 Boys' bodies**, **💭 Feelings**, **🧼 Taking care**. Chip labels follow the teacher's Wording setting.
- Shelf: question cards in a grid (two or three columns), each card one question with a small topic icon and the note "Lots of kids wonder this." Cards whose topic the teacher turned off do not appear.
- Tap a card: it opens to an answer panel beside the shelf (over it at narrow widths): the question as a heading, the answer (2 to 4 sentences), a "Good to know" line where Content has one, and at the bottom "Still wondering? Ask a parent, the school nurse or another adult you trust." Buttons **◀ Back to questions**, **Next question ▶** (next in the current filter).
- Answers are not spoken out loud unless the student presses Read, so nothing plays aloud by surprise on a laptop.

### Age ribbon
- Stage: a ruler from age 7 to 18 across the top. Under it, lanes of soft bands (Content, "Age ribbon"), each a rounded bar from its earliest to its latest common age, with a darker dot where a source gives a typical peak or average. Lanes are grouped: **Changes for everyone**, **Girls' bodies**, **Boys' bodies** (labels follow Wording; lanes the teacher turned off are hidden).
- **Pick an age** slider (7 to 18, default 10) draws a vertical line through every lane. The panel lists each band the line crosses: "At 10, for some kids: breast buds may start; growth spurt may start; body hair may start." and, below, the bands that usually come later or earlier: "Usually later: wet dreams (13 to 17)." Every list ends with: "Some kids your age have started some of these, some have not. Both are normal."
- **Same age, different clocks**: a row of five painted kids (Art; cutouts, full body, fully clothed in loose everyday clothes, five different heights) all labeled "Age 11", each with a little clock icon (code) set to a different time. A caption: "Five kids, all 11, all normal." Tapping a kid shows one line: "This one hasn't started yet," "This one started at 9," and so on (Content). Height, hair, skin tone and clothes colors are the only differences painted; no body changes are shown in any picture.
- Tap any band to open its card (same answer panel as Questions).

### Who can I ask?
- Five people cards (a small painted picture of a place or object from Art, title, one line): **Parent or caregiver**, **School nurse**, **School counselor**, **Doctor or health care provider**, **Teacher or coach**.
- **Ways to start** (three sentence starters, each on its own card): Content.
- **The class question box** card: "Your teacher may have a question box in the classroom. Write your question on a slip of paper. You don't need to write your name." (Hidden if the teacher sets Question box: Off.)
- **Private is okay** card: "You don't have to talk about your body with friends if you don't want to. You can read and learn on your own, and ask when you're ready."

### For teachers (a panel that slides over the right side; Esc or **Done** closes it)
- **Topics shown**: switches for **Girls' bodies**, **Boys' bodies**, **Periods**, **Erections and wet dreams** (each on by default; Changes for everyone, Feelings and Taking care are always on). Turning off Girls' or Boys' bodies hides its lane, chip and cards; Periods and Erections and wet dreams hide only the cards and bands marked with them.
- **Wording**: **Girls and boys** (default) or **Body parts** (chips read "Bodies with ovaries" and "Bodies with testicles", and answers use the matching wording given in Content).
- **Question box card**: On / Off.
- **Print question slips**: prints one page of 12 blank slips ("My question:" and lines, no name line) for the teacher's paper box. Nothing is filled in on screen.
- **Reset settings**. Settings are saved on this device in localStorage `guqa-settings` (try/catch) because they are the teacher's setup; nothing a student does is stored.
- A note: "Check your district's policy before class. Parents and caregivers can preview this tool at the same address."

## Content

### Questions and answers
Each line: topic, question, answer. Text in [brackets] is the Body parts wording.
Changes for everyone:
1. What is puberty? / Puberty is the time when your body slowly changes from a kid's body into an adult's body. Chemicals your body makes, called hormones, start it. It takes a few years.
2. When does puberty start? / It usually starts between ages 8 and 13 for girls [bodies with ovaries] and between 9 and 14 for boys [bodies with testicles]. Starting earlier or later than a friend is normal. Good to know: Doctors like to know if changes start before age 8 or 9, or haven't started by about 13 or 14, so they can check that all is well.
3. Why am I growing so fast? / Most kids have a growth spurt during puberty, when they grow taller faster than before. Girls' [Ovary bodies'] growth spurts often come earlier than boys' [testicle bodies'].
4. Why do I sweat more and smell different? / Sweat glands get more active in puberty, and sweat can start to smell. Washing every day, especially under your arms, and wearing clean clothes help. Deodorant can help too.
5. Why am I getting pimples? / Hormones make your skin make more oil, which can clog pores and cause pimples. Acne is very common in teens. Wash your face gently and try not to pick or squeeze pimples.
6. Will I grow hair in new places? / Yes. Hair grows under the arms and around the private parts for everyone. Hair on the legs often gets darker. Many boys [testicle bodies] also grow hair on the face and chest later.
7. Why do my friends look so different from me? / Everyone starts and moves through puberty at their own pace. At 11, one kid may not have started and another may be halfway through. Both are normal.
8. Am I normal? / If you are healthy, starting early, late or in between is usually normal. If you are worried, a doctor or the school nurse can check and answer your questions privately.
Girls' bodies (or "Bodies with ovaries"):
9. What usually happens first for girls [in bodies with ovaries]? / Usually breast buds: small, sometimes sore bumps under the nipples. One side can start before the other. That is normal.
10. What is a period? (Periods) / A period is when a small amount of blood and tissue from the lining of the uterus leaves the body through the vagina. It lasts a few days and comes about once a month. It is a normal, healthy part of growing up.
11. When will I get my first period? (Periods) / Often about 2 years after breast buds start. It can come as early as about 9 or as late as about 15. Good to know: No one can tell the exact day, so it can help to keep a pad in your backpack.
12. What if my period starts at school? (Periods) / Tell the school nurse or a teacher you trust. They help with this all the time and can give you a pad and help you feel comfortable.
Boys' bodies (or "Bodies with testicles"):
13. What usually happens first for boys [in bodies with testicles]? / Usually the testicles and the skin around them grow bigger. Then the penis grows, and hair starts to grow.
14. Why does my voice crack? / Your voice box grows and your voice gets deeper. While it changes, it can crack or squeak for a while. That is normal and it settles down.
15. What are erections and wet dreams? (Erections and wet dreams) / An erection is when the penis gets stiff. It can happen on its own, and that is normal. A wet dream is when a little fluid called semen comes out during sleep. It is normal and not something you can control.
16. My chest feels puffy. Is that okay? / Some boys [testicle bodies] get a little swelling under the nipples during puberty. It is common and usually goes away on its own. A doctor can check if you are worried.
Feelings:
17. Is it normal to feel moody? / Yes. Hormones and all the changes can make feelings go up and down fast. Sleep, moving your body and talking to someone you trust help.
18. Why do I care more about how I look? / Lots of kids think more about their looks during puberty. Bodies come in all shapes and sizes. If worries about your body or food take up a lot of your thoughts, tell a trusted adult.
19. Is it okay not to want to talk about it? / Yes. Your body is private. You can read and learn on your own and ask questions when you are ready.
Taking care:
20. Why am I so tired? / Growing takes energy. Kids 6 to 12 need 9 to 12 hours of sleep a night, and teens need 8 to 10.
21. What helps my body while it grows? / Sleep, being active every day, eating a mix of foods from all the food groups and drinking water. A daily shower or bath helps with sweat and oil.

### Age ribbon (lane, band ages, dot, topic tag)
- Changes for everyone: Puberty starts (girls 8 to 13, boys 9 to 14, drawn as two overlapping bands in the two lane colors; Wording applies).
- Girls' bodies: Breast buds start (8 to 13); Body hair grows in (9 to 14: starts about 9 to 10, adult pattern by 13 to 14); Growth spurt (9.5 to 14.5, dot at 12); First period (9 to 15, about 2 years after breast buds; Periods).
- Boys' bodies: Testicles grow (9 to 14); Voice deepens (with penis growth, drawn 11 to 15, label "while the penis grows"; tool's own drawing range, labeled "about"); Body and face hair (12 to 18); Growth spurt (10.5 to 18, dot at 14); Wet dreams start (13 to 17, dot at 14.5; Erections and wet dreams).
- The voice band's ages are the tool's own drawing of "at the same time as the penis grows" and carry the word "about" on screen; every other band is from the sources.

### Same age, different clocks (figure lines)
1. "This one hasn't started yet." 2. "This one started at 9." 3. "This one started at 10." 4. "This one just started." 5. "This one started at 8." (All five: "Age 11. Normal.")

### Ways to start
- "Can I ask you something private about growing up?"
- "I read about puberty and I have a question."
- "Something about my body is changing and I'm not sure if it's normal."

## Interactions in detail
- Filtering by chip keeps the open answer if it is in the filter, else closes it. Next question wraps to the first card in the filter.
- Keyboard: arrow keys move between cards; Enter opens; Esc closes the answer.
- Age slider: arrow keys step 1 year, Page Up/Down 2 years; the line, the panel list and the five figures' caption update together. With Motion off the line jumps instead of gliding.
- For teachers settings apply live (shelf, chips, lanes and wording change at once) and survive reload; Reset settings returns every default.
- No text input anywhere. No record of which cards were opened, nothing in localStorage except `guqa-settings` and the kit's Motion.
- Sizes: at 1366x768 the chips, two rows of cards and an open answer are visible together; the Age ribbon shows every lane and the slider without scrolling. In the 680x425 preview the shelf shows at least six cards with 14 px text. At 375 wide the answer opens full width over the shelf with Back at the top.

## Look
- Accent `--brand` #8e4a7a (soft mauve: calm and private), on its own light `:root`: paper #fbf6f8, ink #2b2230, muted #665a66, line #ead9e2, focus #2f5bd3, card #ffffff.
- Contrast: accent on white 6.16:1, on paper 5.76:1; white on accent 6.16:1; ink on paper 14.29:1; muted on paper 6.10:1.
- Lane colors (bands are shapes, each also labeled in words): Everyone #6aa36f sage, Girls' bodies #d9822b amber, Boys' bodies #3f7cc4 blue; band text is ink on a 20 percent tint of the lane color.
- Rounded cards, generous spacing, no bright alerts; the age line is the accent.
- Group siblings: body-systems-tour orange, first-aid-responder mint, meal-and-move-planner sky blue, health-claim-checker yellow. 3-5 health neighbors are teal, raspberry and green.

## Art
12 images, 5 with people. One calm style for all: "soft pastel colored-pencil illustration, warm and gentle"; cutouts add "plain white background". No anatomical drawings: all body changes are described in words, and no picture shows a body change.

The five kids (people: true: Gemini via `scripts/art.py`, which is set aside for now, so these wait on Cory; every one needs Cory's review before launch). Kit rule: one shared prompt, "A smiling 11-year-old kid standing relaxed, full body, front view, fully clothed in loose everyday clothes and sneakers, soft pastel colored-pencil illustration, plain white background", plus each kid's own line below; 3:4; cutout yes; people yes; used in Same age, different clocks. Sizing rule: each is scaled to its own height in the row (five different heights, not in height order, so height does not line up with the clock lines), feet on one baseline.
- gu-kid-1: short curly black hair, brown skin, a yellow t-shirt and jeans.
- gu-kid-2: a long brown ponytail, light skin, a green hoodie and gray joggers.
- gu-kid-3: short straight black hair, light brown skin, a red striped shirt and shorts.
- gu-kid-4: braids, dark brown skin, a purple sweatshirt and jeans.
- gu-kid-5: short wavy blond hair, light skin, a blue t-shirt and cargo pants.

Who can I ask? and the two help cards (local FLUX, `scripts/localart.py`; places and objects only, no people; 4:3; cutout no):
- gu-ask-home: "A kitchen table with two mugs and a plate of cookies by a sunny window"; people no; Parent or caregiver card.
- gu-ask-nurse: "A school nurse's office with a neat cot, a first aid kit on a shelf and a jar of bandages"; people no; School nurse card.
- gu-ask-counselor: "A cozy school counselor's office corner with two soft armchairs, a potted plant and a box of tissues"; people no; School counselor card.
- gu-ask-doctor: "A stethoscope and a clipboard with blank paper on a tidy doctor's desk"; people no; Doctor or health care provider card.
- gu-ask-coach: "A whistle on a lanyard and a red ball beside an apple on a wooden desk"; people no; Teacher or coach card.
- gu-question-box: "A small shoebox covered in pastel paper with a slot in the lid, a few folded blank paper slips beside it"; people no; The class question box card.
- gu-journal: "A closed notebook with a ribbon bookmark and a pencil on a soft knitted blanket"; people no; Private is okay card.

Drawn in code: the cards, chips, icons, clock icons, the age ribbon (a chart), the slider and preview.svg.

## Voice
`clear-teacher` (Iapetus): "Say clearly and kindly, like a patient elementary school teacher." Different from body-systems-tour (upbeat-guide), fitness-circuit (big-sister) and playbook (lively-host). `Curio.voice`; every line is a how line, spoken once per load, then hint only.
| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wQ | how | entering Questions, first time | Welcome. Tap a question card to read the answer. Tap Read if you want to hear it. | a card or chip tapped; mode left |
| wRibbon | how | entering Age ribbon, first time | Drag the Pick an age slider to see which changes might be starting. Normal is a range. | the slider moved; mode left |
| wAsk | how | entering Who can I ask?, first time | Here are people you can ask, and some ways to start. Tap Read to hear them. | Read tapped; mode left |
| howChip | how | the first time an answer is closed | Tap a topic to show only those questions. | a chip tapped |
Answers, bands and kid lines are never spoken by themselves; Read speaks the open answer, else (in Who can I ask?) the cards in order, else the hint. There are no event lines.

## Family engine
none

## Sources
- NHES 2024 (SHAPE America), Standards 1 and 3: https://www.shapeamerica.org/standards/health/
- Puberty starts 8 to 13 (girls) and 9 to 14 (boys); hormones; early (before 8 or 9) and late (none by about 13 or 14) are reasons to see a doctor: NICHD, "Puberty and Precocious Puberty": https://www.nichd.nih.gov/health/topics/puberty/conditioninfo
- Order and ages of changes (breast buds from about 8; body hair about 9 to 10 to adult pattern 13 to 14; first period about 2 years after breast buds, about 9 to 15; girls' growth spurt 9.5 to 14.5, peak about 12; testicles from about 9; voice changes as the penis grows; boys' body and face hair from about 12 to 17 or 18; boys' growth spurt about 10.5 to 18, peak about 14; wet dreams typically 13 to 17, average about 14.5): MedlinePlus, "Adolescent development": https://medlineplus.gov/ency/article/002003.htm
- Puberty overview, sweat and body odor, voice, moods: MedlinePlus, "Puberty": https://medlineplus.gov/puberty.html
- Periods: MedlinePlus, "Menstruation": https://medlineplus.gov/menstruation.html
- Acne in teens, hormones and oil, wash gently, don't pick: NIAMS, "Acne": https://www.niams.nih.gov/health-topics/acne
- Breast swelling in boys during puberty is common and usually goes away: MedlinePlus, "Breast enlargement in males": https://medlineplus.gov/ency/article/003165.htm
- Sleep 9 to 12 hours (6 to 12) and 8 to 10 hours (13 to 18): CDC, "About Sleep": https://www.cdc.gov/sleep/about/index.html
- Daily activity and food groups (question 21): CDC, "Physical Activity Facts" (children and adolescents 60 minutes a day): https://www.cdc.gov/physical-activity-education/data-research/facts-stats/index.html; USDA MyPlate: https://www.myplate.gov/
- The build agent checks every answer sentence against these pages and edits wording to match them, citing the page per card in a comment.

## Done when
1. No text field exists anywhere in the tool (check the DOM); localStorage holds only `guqa-settings` and `curio-motion`.
2. All 21 questions appear with All; each topic chip shows exactly its cards; Next question wraps.
3. Turning off Periods hides questions 10 to 12 and the First period band; turning off Boys' bodies hides questions 13 to 16, the boys' lane and chip, and the boys' half of the "Puberty starts" band.
4. Wording: Body parts changes chips, lane names and every bracketed phrase; Girls and boys restores them.
5. Age slider at 10 lists exactly the bands that contain 10 (girls' puberty start, breast buds, body hair, girls' growth spurt, first period, boys' puberty start, testicles grow) and puts boys' growth spurt, voice, body and face hair and wet dreams under "Usually later".
6. Answers never auto-play; Read speaks the open answer; welcome lines speak once per load.
7. Print question slips prints 12 blank slips with no name line.
8. At 1366x768 chips, cards and an open answer fit without scrolling; at 375 wide the answer covers the shelf with Back reachable; keyboard alone can open, read and close every card.
9. Focus: in Questions the open answer is the largest, clearest panel beside the shelf; in Age ribbon the age line and the list it crosses are the center of the screen at 1366x768 and 680x425.
10. Tap while it plays: while Read is speaking, a tap on another card, Back, a chip, the slider or a mode stops the speech at once; nothing plays aloud that the student did not ask for.
11. Art: the five kids are fully clothed, differ only in height, hair, skin tone and clothes colors, and are approved by Cory before launch; the seven place and object pictures show no people and no lettering.

## Open questions
1. Question box (concept change): the concept had an anonymous question box stored only locally. Per the wave rule, there is no text box at all. In its place: 21 pre-written real-kid questions, a card pointing to the teacher's paper box, and a teacher button that prints blank slips. OK, or drop the print button too?
2. Default wording: "Girls and boys" (common in district curricula) or "Body parts" (inclusive of every body)? The tool offers both; Cory picks the default.
3. Default topics: Periods and Erections and wet dreams are on by default. Some districts teach these only in grade 5 or in separate groups. Keep them on, or default them off for teachers to turn on?
4. Parent preview: should the tool page carry a line for parents ("Preview every card at this address; nothing your child does is stored")?
5. Same age, different clocks now asks for five painted kids (people: true, Gemini, your review) in place of the plain code figures. OK, or keep plain shapes for this sensitive tool?
