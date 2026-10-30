# Speech Coach

## One idea
A talk is a plan in time: build it as a run sheet where every section has its words, its slide and its seconds, rehearse it out loud while tapping through the sections, and the run sheet comes back marked with your real pace section by section (words in that section over the time you took), the slides that sat up too long or that only repeated what you said, and the places a listener got lost, so each run is a trial you change one thing in and run again.

## Not like
- pacing-strip (ela 9-12, lab, this group): pacing of a written scene, words against story time. Here pacing is spoken: words against clock time, measured from a live rehearsal.
- rhetorical-situation-simulator (ela 11, simulator, spec): turns the dials of a famous speech's situation to see which lines strain. Here the student's own talk is planned, rehearsed and measured; the situation is one of three real tasks with time limits.
- source-mixer (ela 11, data, spec): mixes a chart, a broadcast and a photo into one research answer. Here media are slides in a live talk, judged by the job each does for a listener and whether it competes with the speaker's voice.
- argument-map (ela 12, builder, spec): rebuilds a written essay's structure. Here the structure is heard: signposts and link words a listener can follow without seeing anything.
- personal-essay-studio (ela 11, studio, this group): written and private. Here nothing is written to be read; it is spoken.
- ad-agency (ela 12, tycoon, spec): persuasion tricks and how to catch them. Here persuasion is honest: a claim, reasons, sourced evidence and the other side.

## Who and how
- Grade 12 ELA. Module: Formal Presentations (Speaking and Listening).
- Topic line: "rehearsing a presentation".
- Driver: students on laptops, alone, or with a partner beside them as the listener. 25 to 45 minutes (build or load a talk, then three or more runs).
- Standards: SL.11-12.4 (present information, findings and evidence with a clear perspective, so listeners can follow the line of reasoning, alternative or opposing perspectives are addressed, and organization, development, substance and style suit purpose, audience and a range of formal and informal tasks): the run sheet's roles and signposts, the Thread view and Listener test, the required Other side check, the three tasks with their limits and register, and pace and delivery in Review. SL.11-12.5 (strategic use of digital media, textual, graphical, audio, visual and interactive, to enhance understanding of findings, reasoning and evidence and to add interest): the slide maker (words, chart, picture, quote, ask the room, blank), each slide's job, the Busy and Reading slide checks, and the slide timer in Review.
- Privacy line on every screen: "Your talk and your run numbers stay on this device. The microphone is optional and never records."
- tool.json: driver "students", minutes "25-45", modes ["Build", "Rehearse", "Review"], grades_label "Grade 12". Kit starter plus `kit:theme-912`.

## Screens and modes
Header: title "Speech Coach", small line "Plan it. Run it. Read the marks."; talk picker **Sample: Push the first bell** / **My talk**; mode buttons **Build** (opens first), **Rehearse**, **Review**; Motion, Sound, Read. Panel: `#hint`, the task card, total planned time against the limit ("1:55 of 2:00"), **Save run notes**, **Clear my talk** (asks Yes / No).

### Task card (panel, all modes)
Three tasks, picked from chips; each sets a time limit, a register note and a goal:
- **Board comment** (formal, 2:00 hard limit, the sample's task): "Speak to officials. Name your request early. Stop at the limit."
- **Club pitch** (informal, 1:00): "Talk to classmates. Keep one reason and the ask. Cut the rest." Sections marked **Must keep** can't be cut.
- **Class presentation** (formal, 4:00 to 5:00): "Develop it: add a reason or more evidence, and slides that show it."
Switching tasks keeps the talk; the run sheet shows over or under the new limit.

### Build (opens first)
Focus: the selected section card and its slide, side by side in the middle; the rest of the run sheet is a narrow scrolling column of collapsed cards.
- Left: the run sheet, a column of section cards in order. Each card: a role chip (**Opening**, **Claim**, **Reason**, **Evidence**, **Other side**, **Answer**, **Close**), a **Signpost** box (the first sentence a listener hears in that section), the **Script** box (full words or notes), a word count, a planned time (auto from words at 150 words per minute, editable), **Must keep**, and a link-word chip into the next section (**because**, **for example**, **but**, **so**, **therefore**, **finally**).
- **Add section**, **Move up**, **Move down**, **Delete section** (asks).
- Right: the slide for the selected section, made with the **Slide maker**: a kind (**Words**, **Chart**, **Picture**, **Quote**, **Ask the room**, **Blank**) and a **Slide's job** chip (**Shows evidence**, **Shows a pattern**, **Gives a picture**, **Gives the key words**, **Asks the room**, **Rests the eyes**). Chart: a bar chart from up to 5 labeled numbers the student types, with a required source line. Picture: one of the tool's three public-domain artworks (Art) with its credit, or none. Quote: text plus a required source line. Ask the room: a question shown large, for a show of hands. Blank: a dark slide on purpose.
- Slide checks under the slide (readings, never errors): **Busy slide** when it holds more than 20 words ("Listeners can't read 47 words and hear you at once.", with the slide's own count). **Reading slide** when more than 60 percent of its words are also in the section's script ("This slide says what you say. Give it a different job."). **No source** on a chart or quote without a source line. The thresholds are rules of thumb set for this tool, and the screen says so.
- **Thread view** (button): only the signposts and link words, in order, as one paragraph. Prompt: "If a listener heard only these lines, could they follow you?" **Listener test**: the student types the whole talk's point in one sentence from the thread alone, then compares it with the Claim card.
- **Other side check** (always on): "No Other side section yet. Listeners who disagree will notice." until a section has that role; then "Your Other side is answered" when an Answer section or link word "but" follows it.

### Rehearse
- Focus: the current section's signpost and the Next button, the biggest things on screen. Full stage, dark: the painted empty house (Art) seen from the stage fills the back, dimmed under a solid script panel, so the student talks to a room of empty seats; on it the current section's signpost large, its script or notes below (toggle **Script / Notes only / Nothing**), the slide preview at the right, a section timer and the total clock. A thin strip at the bottom shows every section as a block, planned width against elapsed.
- **Start** shows a 3-2-1 count (visual), then the clock runs. The student speaks out loud and presses **Next** (Space or the big button) at the end of each section; the last Next ends the run. **Pause** (P) and **Abandon run** (asks).
- **Listener pad** (right edge, for a partner beside the speaker; keys F, L, H, N): **Filler** (um, uh, like, you know), **Lost me**, **Couldn't hear**, **Nice moment**. Each tap is stamped with the section and second. A solo speaker ignores it.
- **Listen for pauses** (off by default): asks for the microphone, shows a live level bar, and counts long pauses (more than 2 seconds of quiet while the clock runs) and the share of talk time. The line beside it: "Measuring loudness only, right now. Nothing is recorded or saved." It turns off when the run ends or the mode changes.
- The tool never listens for words: speech-to-text in browsers can send audio off the device, so fillers come from the listener pad or the self-check.
- No voice lines play during a run: Start stops any line that is speaking and clears the queue. The run is the student's own talk (up to 5:00 for Class presentation), not an auto-play; Next, Pause, Abandon run and the listener pad respond at once at every moment of it.

### Review
Focus: the marked run sheet, full width in the middle; the Runs table sits below it.
- The run sheet comes back marked, one row per section: planned time, actual time, pace in words per minute with a band word (**slow** under 110, **steady** 110 to 170, **fast** over 170), listener marks as icons at their second, long pauses if measured.
- **Slide timer**: each slide's time on screen and its word count, with a reading when a Busy slide was up under 10 seconds ("Slide 5: 47 words, up 8 seconds").
- **Self-check** (solo, after every run): "How many fillers do you think you said? None / a few / many", "Tap any section where you stumbled", "Did you finish inside the limit?" (filled in for you). Kept with the run.
- **Runs** table (lab notebook): up to 8 runs with total time, over or under the limit, slowest and fastest section, fillers per minute (listener taps over minutes), Lost me count, and a **What I changed** note per run. **Compare runs** stacks two run strips.
- **Conclude** box: "What one change helped most? What's your next trial?"

## Content
### Sample talk: Push the first bell (original, written for Curio Class; task Board comment)
Words counted on spaces; times at 150 words per minute, rounded to 5 seconds.
1. Opening (45 words, 20 s). Signpost: "Raise your hand if you were awake before six this morning." Script: "Raise your hand if you were awake before six this morning. Keep it up if you felt fully awake by first period. Most hands go down on that second question, and there is a reason. It isn't laziness. It's biology, and it's the bell schedule." Link: so. Slide: Picture, maid-asleep, job Gives a picture.
2. Claim, Must keep (35 words, 15 s). Signpost: "So here is my claim." Script: "So here is my claim: our district should move the first high school bell to 8:30 a.m. or later. I'll give you two reasons, answer the biggest objection, and then ask you for one thing." Link: because. Slide: Words "First bell: 8:30 a.m." over wall-clock, job Gives the key words.
3. Reason (51 words, 20 s). Signpost: "First reason: we don't get enough sleep." Script: "First reason: we don't get enough sleep. The American Academy of Sleep Medicine says teenagers need eight to ten hours a night. But when the CDC surveyed high school students in 2015, about seven in ten said they slept less than eight hours on school nights. That's most of this room." Link: and. Slide: Chart, two bars "Less than 8 hours: 72.7" and "8 hours or more: 27.3" (percent of US high school students on school nights, 2015), source line "CDC, MMWR, 2018", job Shows evidence.
4. Reason (52 words, 20 s). Signpost: "Second reason: it isn't a matter of just going to bed earlier." Script: "Second reason: it isn't a matter of just going to bed earlier. The American Academy of Pediatrics explains that in the teen years the body clock shifts later, and many teenagers have trouble falling asleep before eleven. That's why the Academy recommends that middle and high schools start at 8:30 or later." Link: but. Slide: Quote "Middle and high schools should aim to start no earlier than 8:30 a.m." (wording checked against the AAP statement at build, or shown as the plain paraphrase "AAP: start at 8:30 a.m. or later"), source line "American Academy of Pediatrics, 2014", job Shows evidence.
5. Other side (70 words, 30 s). Signpost: "Now the biggest objection." Script: "Now the biggest objection. Later start times can mean new bus routes, and they push practices and after-school jobs later into the evening. Those costs are real. But they can be worked out. In 2019, California passed a law that has most high schools start no earlier than 8:30, beginning with the 2022-23 school year. If a whole state can rework its buses and schedules, our district can study it." Link: so. Slide (a deliberate Busy and Reading slide, 47 words by the tool's own word rule, 46 of them in the script, 98 percent; the lone "=" is not a word): "Objection: buses. Later start = new bus routes. Practices and after-school jobs end later in the evening. Those costs are real. California law (2019): most high schools start no earlier than 8:30, beginning 2022-23. If a whole state can rework buses and schedules, our district can study it." Job Shows evidence. A tip on the sample: "This slide has a problem on purpose. Find it, fix it, and run again."
6. Close, Must keep (42 words, 15 s). Signpost: "So here is my one request." Script: "So here is my one request. Sign our letter asking the school board to study an 8:30 start for next year. A later bell won't fix everything. But it would let us show up to first period awake, and that's worth studying." Slide: Picture, harvesters, job Gives a picture, caption "Bruegel painted a harvester asleep at noon, 1565."
- Totals: 295 words, planned 2:00 (120 s); the Board comment limit is 2:00.
- Context card for the sample: "The talk is made up; the facts in it are real and sourced. Sleep needs vary from person to person."

### Pace bands and the 150 words per minute default
- On screen, About pace: "A common figure for conversational English is about 150 words per minute. The slow and fast bands here are rules of thumb for a talk, not rules." (Sources.)

## Interactions in detail
- Pace for a section = words in its script divided by actual seconds, times 60, rounded to a whole number. With Notes only or Nothing showing, pace still uses the script's words (the plan) and the panel says so: "Pace is measured against your script."
- Planned time default = words / 150 x 60, rounded to the nearest 5 seconds, minimum 5. Editing a planned time marks it "set by you" and stops auto-updates.
- Slide words: split on spaces after removing punctuation except colons and hyphens inside words; case ignored. Reading slide percent = slide words that also appear in the section's script / all slide words.
- Listener taps and pause counts are stored only as numbers with section and second. Mic: `getUserMedia({audio:true})`, an AnalyserNode RMS level every 100 ms; quiet = level under a threshold set from the first 2 seconds of the run (room noise times 1.5); a long pause is 2 seconds or more of quiet. The stream is stopped and released when the run ends, on Abandon, on mode change and on page hide. No audio is kept in any variable past the current frame.
- Runs, talk and notes save to localStorage `speech-coach:v1` (try/catch): the talk (sections, slides), runs (numbers, self-checks, notes). If storage fails, a banner says "This browser isn't saving. Your runs will be lost when you close the tab." Clear my talk asks first. The sample has **Reset sample**.
- Keys: Space Next, P pause, F L H N listener pad, Esc leaves Rehearse after the run.
- Sizes: Rehearse fills the stage at real pixel size; the signpost is at least 28 px at 1366x768 and 18 px at 680x425; at 680x425 Next, the clock and the slide preview are visible without scrolling. At 760 and below the slide preview moves under the script and the listener pad becomes a row of four 56 px buttons. At 375 Build shows one section card at a time with **Previous / Next section**. No horizontal page scroll.
- Motion off: the 3-2-1 count is static numbers; the timeline strip jumps instead of growing.

## Look
- Accent `--brand #5ee07a` (cue-light green: header rule, Start, Next, active mode, planned-time marks) on the kit `theme-912` base. Rehearsal scene: the painted empty house behind a solid script panel `#0d1219` at 92 percent, script text `--ink` #e8edf3. Pace bands with words and glyphs: slow ◀ `#ffd166`, steady ● brand, fast ▶ `#ff8a8a`.
- Contrast (WCAG 2.1): brand on panel #141b25 10.24:1, on sec-bg #18202b 9.70:1, on stage 11.11:1; brand-ink #1c1203 on brand 10.92:1; script ink on stage 15.96:1; slow #ffd166 on panel 12.0:1; fast #ff8a8a on panel 7.63:1.
- Different from neighbors: word-family-tree new-leaf green #a6d84a (dE 31, yellower), pacing-strip mint #3fe0c5 (dE 39), argument-map cyan, ad-agency acid green #a3ff19 (brighter, yellower), premise-inspector olive gold, and this group's accents. world-lit-atlas #8ff05a (dE 23) is not a neighbor.

## Art
4 images. Three are museum photographs of public-domain artworks, already saved in `tools/speech-coach/art/` with `public-domain.json` (no network at run time); they are not generated, so they need no art tool, but two show people and Cory sees them in review. One is painted with local FLUX (`scripts/localart.py`), no people.
- maid-asleep (`pd-met-437878.webp`): Johannes Vermeer, A Maid Asleep, ca. 1656-57, The Met, object 437878 (accession 14.40.611); 4:3 crop of the full painting; cutout no; people yes (a painted figure in a public-domain work, not generated); the Opening slide's picture and the Slide maker's picture shelf.
- harvesters (`pd-met-435809.webp`): Pieter Bruegel the Elder, The Harvesters, 1565, The Met, object 435809 (accession 19.164); 16:10 crop centered on the resting harvesters under the tree; cutout no; people yes (painted figures in a public-domain work, not generated); Close slide and picture shelf.
- wall-clock (`pd-aic-57819.webp`): Wall Clock, c. 1735-40, case by Jean-Pierre Latz, Art Institute of Chicago, object 57819; 3:4, full object on a dark ground; cutout no; people no; behind the Claim slide's words and in the picture shelf.
- sc-empty-house: rows of empty red velvet seats in a dim school auditorium seen from the front of the stage, a soft spotlight haze in the air, the back rows fading into darkness; 16:9; cutout no; people no; the Rehearse backdrop behind the script panel.
- Drawn in code: run sheet, slides' words, charts, the timeline strip, listener pad, pace marks, Review tables, preview.svg.

## Voice
Bank voice `easy-coach` (Umbriel), style "Say in an easy-going, encouraging way, like a relaxed speech coach at rehearsal." No neighbor or batch tool uses it (pacing-strip playful-friend, rhetorical-situation-simulator smooth-narrator, argument-map clear-teacher). The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.talk`. **Rehearse is silent once Start is pressed**: no line plays during a run. The talk is never voiced.
- w-build (how; Build welcome; stale once any box is typed in): "Each card is one section. Type its signpost first, then its words. Then make its slide on the right."
- slide (how; first Slide maker opened; stale once a job chip is set): "Tap a slide kind, then tap its job. A slide should do something your voice can't."
- busy (how; first Busy or Reading slide reading; stale when that reading clears): "This slide competes with you. Cut its words, or tap a different job."
- thread (how; first Thread view; stale once the Listener test box has text): "These are only your signposts. Type the talk's point in the Listener test box from them alone."
- other (how; first time the Other side check shows; stale once a section has that role): "Tap Add section and set its role to Other side. Then answer it."
- w-rehearse (how; Rehearse welcome, before Start; stale once Start is pressed): "Press Start and talk out loud. Press Next or Space at the end of each section."
- mic (how; first Listen for pauses on, before Start; stale once Start is pressed): "The microphone only measures loudness. Nothing is recorded."
- w-review (how; Review welcome; stale once a What I changed note has text): "Each row shows your real pace. Find the fastest section, then type what you'll change."
- runsaved (event; every finished run, on entering Review; stale when another run starts): "Run saved. Write what you'll change, then run it again."
- over (event; a run ends over the task's limit; stale when another run starts): "You ran over the limit. Find a section to cut or tighten."

## Family engine
None.

## Sources
- Standards: CCSS ELA SL.11-12.4 and SL.11-12.5, https://www.thecorestandards.org/ELA-Literacy/SL/11-12/.
- Teen sleep need, 8 to 10 hours per 24 hours for ages 13 to 18: Paruthi S. et al., "Recommended Amount of Sleep for Pediatric Populations," Journal of Clinical Sleep Medicine 12(6), 2016 (American Academy of Sleep Medicine consensus); also CDC, "About Sleep," https://www.cdc.gov/sleep/.
- 72.7 percent of US high school students reported less than 8 hours of sleep on school nights in 2015: Wheaton A.G. et al., "Short Sleep Duration Among Middle School and High School Students, United States, 2015," MMWR 67(3), January 26, 2018, https://www.cdc.gov/mmwr/volumes/67/wr/mm6703a1.htm. Confirm the figure at build; the chart shows "data as of 2015".
- Body clock shift in adolescence, trouble falling asleep before 11 p.m., and the 8:30 a.m. recommendation: American Academy of Pediatrics, Adolescent Sleep Working Group, "School Start Times for Adolescents," Pediatrics 134(3), 2014, https://publications.aap.org/pediatrics/article/134/3/642/74175. Confirm the exact wording for the Quote slide at build.
- California SB 328 (2019), Education Code section 46148: most public high schools start no earlier than 8:30 a.m. from the 2022-23 school year, with rural exemptions: California Legislative Information, https://leginfo.legislature.ca.gov/ (bill SB-328, 2019).
- About 150 words per minute for conversational English: National Center for Voice and Speech, "Voice Qualities" (rate of speech), https://ncvs.org/; confirm at build, and if not plainly stated, keep the line as "a common rule of thumb" with no source named.
- Artworks: https://www.metmuseum.org/art/collection/search/437878 ; https://www.metmuseum.org/art/collection/search/435809 ; https://www.artic.edu/artworks/57819 (all public domain, open access; checked 2026-10-27).
- The sample talk, task cards and all tool text: original, written for Curio Class.
- Checks run 2026-10-29 (Python, scratch sc.py): the six scripts split on spaces give 45, 35, 51, 52, 70 and 42 words (295), planned 20, 15, 20, 20, 30, 15 s (2:00) by the rounding rule, all as stated. The scripted run gives 108 slow, 140, 180 fast, 136, 140, 168 and 2:05, as in Done when. Slide 5 by the tool's word rule has 47 words (48 pieces on spaces, but "=" is not a word), 46 of them in its script, 98 percent; the old 48 words and 92 percent were wrong and are fixed. The Review example "up 14 seconds" broke its own under-10-seconds rule; now 8 seconds. Chart bars 72.7 plus 27.3 make 100. Contrast ratios recomputed; all match Look.

## Done when
- The sample loads with six sections, 295 words and a planned total of 2:00 against the Board comment limit; switching to Club pitch shows "over by 1:00" and Must keep blocks deleting the Claim and Close.
- Slide 5 shows Busy slide (47 words) and Reading slide (98 percent); removing slide 3's source line shows No source.
- A scripted run (Next at 25, 40, 57, 80, 110 and 125 seconds) gives paces Opening 108 slow, Claim 140 steady, Reason 1 180 fast, Reason 2 136 steady, Other side 140 steady, Close 168 steady, and total 2:05, over by 5 seconds (recompute in Python).
- Listener pad taps land on the right section and second; fillers per minute = filler taps / run minutes.
- With the mic on, a 3-second silence during a run counts one long pause; the mic stream is released when the run ends (check the track's readyState is "ended"); nothing audio is saved in localStorage.
- No voice line plays between Start and the end of a run; pressing Start while the Rehearse welcome is speaking cuts it off at once.
- Focus: Rehearse at 1366x768 shows the signpost and Next as the largest items over the dimmed painted house; Build shows the selected card and its slide side by side; Review the marked run sheet.
- Tapping Next, Pause or a listener pad button at any second of a run takes effect at once (the timer and stamps use the tap time, not the next tick).
- Thread view shows only the six signposts and link words; deleting the Other side section shows the Other side check.
- Runs table keeps up to 8 runs across a reload; Clear my talk asks first; Reset sample restores it.
- At 680x425 and 1366x768, Next, the clock and the slide preview are visible without scrolling in Rehearse; at 375 there is no horizontal scroll.

## Open questions
- [speech-coach] Two of the museum pictures (Vermeer's A Maid Asleep, Bruegel's The Harvesters) show people. They are public-domain paintings, not generated, so the Gemini rule does not apply; are they fine to keep as they are?

Settled:
- No speech-to-text: browsers' recognition can send audio off the device, which the wave's privacy rule forbids; pace comes from script words over section time, fillers from a listener or the self-check, and the optional mic measures loudness only, in memory (wave speaking rule, BASELINE rule 7).
- The sample topic (school start times) touches sleep health; it is factual, calm and sourced to the AAP, AASM and CDC (wave 1 health rule), with no scare framing.
