# Stress Toolkit

## One idea
Run a one-minute experiment on yourself: mark how wound up your body feels, really do one coping tool (slow breathing, tense and release, a five senses check, a worry dump, shake it out, a calm place), mark it again, and a lab notebook builds up showing which tools moved you, because what helps is different for each person and the only way to know is to test it.

## Not like
- calm-corner (K-2 feelings sibling, teacher led): Shelly leads a whole class through five calm-down tools with a class check-in. Here one student runs their own tests, older tools (tense and release, worry dump, calm place), and the result is a personal notebook comparing tools.
- resilience-map (9-12 SEL, explorer): an island map of coping routes split by the part you can change and the part you can't, plus a plan card. Stress Toolkit has no map and no situations: you do each tool for a minute and measure its effect on you.
- mind-map (9-12 feelings sibling): its stress bucket fills with stressors and drains with taps. Here nothing is modeled; the student is the experiment.
- comeback-club (3-5 SEL, creature): coming back from mistakes with a creature. goal-tracker (6-8 PE, creature): activity goals and consistency.
- pressure-point (group sibling): a branching story about refusal. relationship-spectrum (group sibling): healthy to abusive line. screen-week (group sibling): a pretend kid's week as data. This is the only tool in the group where the student does something with their body.

## Who and how
- Grade 6-8, Health, module Mental and Emotional Health (stress, coping and getting help).
- Driver: students on laptops (headphones help for Calm place). A teacher can project one tool and run it with the whole class.
- Minutes: 10-25 (each test is about 2 minutes).
- Standards: NHES.S1 (stress and the body), NHES.S7 (practice health-enhancing behaviors: stress management), NHES.S8 (advocate for self: knowing where to get help); also CASEL.Self-Awareness (noticing how your body feels), CASEL.Self-Management (choosing and testing coping tools).
- Topic line: "stress and coping strategies".
- Modes (tool.json): ["Try a tool", "My notebook", "Why it works"].

## Screens and modes
Header: title "Stress Toolkit" with the topic line under it, mode buttons **Try a tool**, **My notebook**, **Why it works**, then **Motion**, **Sound**, **Read**. Stage left, panel right. A help footer in every mode (see Help footer).

### Try a tool (opens first)
- Focus, home: the open toolbox (painted, Art), center stage, with the seven tool tiles laid in its tray, each tile with its painted icon, name and a one-line "what you do": **Slow breathing**, **Tense and release**, **Five senses**, **Worry dump**, **Shake it out**, **Calm place**, **Talk to someone**. Tiles tested at least once show a small notebook tab with the number of tries.
- A test has three steps shown as a strip at the top of the stage: **1 Before**, **2 Try it**, **3 After**.
  Focus during a test: step 1 and 3, the gauge, big and centered on the stage; step 2, the running tool fills the stage, with Pause, Start over and Stop always live (a tap acts at once, also mid-line).
  1. Before: the body gauge (Content) as five tall buttons from **Calm and loose** to **Revved up**; tap one. **Skip rating** goes straight to step 2 (the test then is not added to the notebook, only counted as tried).
  2. Try it: the tool runs on the stage (Content) with **Pause**, **Start over** and **Stop** in the panel. When it finishes, step 3 opens by itself.
  3. After: the same gauge, with the Before pick outlined. Tap one. The panel shows the change ("2 steps calmer", "about the same", "1 step more wound up") and **Add to notebook** (the default action, Enter), **Try another tool**.
- Talk to someone has no test: it opens a card (Content) and the help footer's More help.

### My notebook
- Focus: the dot chart, the top two thirds of the stage. Stage: a lab notebook page (lined paper, drawn in code). Top: a dot chart with one row per tool and an axis from "more wound up" (right) to "calmer" (left), steps -4 to +4; every test is a dot (shape per tool, never color alone); the average of each row is a short bar. Below it, the table of tests: #, tool, before, after, change.
- Below the table: the **My toolkit** card, listing each starred tool with its how-to line (from Content) and the help footer text; empty until a tool is starred ("Tap a star in the panel to add a tool.").
- Panel: the summary (Interactions), a star toggle per tool "In my toolkit", **Clear notebook** (asks "Clear every test from this page?" with **Clear** and **Keep**).
- A note always visible: "This notebook lives only in this page. Nothing is saved or sent. It clears when you close or reload."
- Empty notebook: "No tests yet. Pick a tool in Try a tool, rate before and after, and your results show up here."

### Why it works
- Focus: the two side by side panels and their meters, filling the stage. Stage: two panels drawn in code (a diagram), **Stress response** and **Relaxation response**, each with three live meters (Breathing, Heart, Muscles) and a thought cloud. A switch in the panel animates from one to the other (with Motion off the meters jump).
- Panel: the cards from Content (what stress is, signs, which tools aim at which part), each a button that highlights the matching meter.

## Content

### The body gauge (the tool's own five steps; numbers 1 to 5 shown on each button)
1 **Calm and loose**: breathing slow, shoulders down. 2 **Mostly settled**. 3 **A bit buzzy**: some fidgeting or a busy mind. 4 **Tight and restless**: tight shoulders or stomach, hard to sit still. 5 **Revved up**: heart going fast, thoughts racing. Each button: number, words, a bar that grows with the step, and a color from slate #3f6fa3 (1) to clay #b5562f (5).
Under the gauge: "This is how your body feels right now, not a score. There is no right answer."

### The tools (timings are the tool's own choices, made to fit about a minute)
- **Slow breathing** (breathing exercise, NCCIH). A dot rides a rolling hill line: up the hill while breathing in, down while breathing out. Pace switch: **4 in, 6 out** (default; 6 breaths, 60 s) or **Box: 4 in, 4 hold, 4 out, 4 hold** (4 rounds, 64 s; holds are flat ledges). Optional **Follow along**: press and hold Space or the big **Hold while breathing in** button; your own trace draws under the guide line in a lighter shade. No score. A soft rising tone on each in-breath, falling on each out (Sound on).
- **Tense and release** (progressive relaxation, NCCIH). A painted wooden artist's mannequin standing (Art) with a soft glow drawn in code over one area at a time: hands ("Make tight fists"), shoulders ("Shrug up to your ears"), face ("Scrunch your whole face"), stomach ("Pull your belly in tight"), feet ("Curl your toes"). Each area: 5 s tense (the glow fills and a ring tightens), 10 s release ("Let it go. Notice the difference."). 75 s total.
- **Five senses** (a mindfulness sense check; CDC lists meditation as a way to cope). Five rows of dots: 5 things you **see**, 4 you can **feel**, 3 you **hear**, 2 you **smell**, 1 slow **breath**. Tap a dot each time you notice one; nothing is typed or recorded. Self paced; **Done** when every dot is filled or at any time.
- **Worry dump** (CDC: keep a journal). A painted paper note card (Art) with the text box drawn on it: "What's on your mind?" (a text box, up to 280 characters, kept in memory only). Then two buttons: **One small step** (a second box: "One small thing I could do next", up to 120 characters) and **Fold it up** (the note card swaps to the painted paper boat, which floats off the stage edge; the text is erased from memory). With One small step, the card shows only the step and then also folds away when the student taps **Done**. Nothing typed is ever kept, printed or shown again.
- **Shake it out** (CDC: move more). A 60 s routine with the painted mannequin, one pose cutout per move (Art), and a ring timer: march in place 20 s, arm circles 10 s, shake out your hands 10 s, reach up and lean side to side 10 s, slow shoulder rolls 10 s. Works seated: a **Seated version** switch swaps in the seated pose set: heel taps for marching, and every other move done sitting.
- **Calm place** (guided imagery, NCCIH). Pick a place: **Beach at sunset**, **Forest after rain**, **Snowy cabin**, **Rooftop at night** (art). 60 s: the picture fills the stage with a slow drift, a synthesized sound bed (waves, dripping and birds, wind and a crackle, distant city hum and crickets), and four prompts 15 s apart: "Look around. What colors do you see?" / "Listen. What's the quietest sound?" / "Is it warm or cool here? Feel it on your skin." / "Take one slow breath. You can come back here any time."
- **Talk to someone** (CDC: talk with people you trust). Card: "Some stress is too big for a one-minute tool, and that's normal. Talking helps. Who could you talk to? A parent or family member, a teacher or coach, the school counselor, a friend who listens." A line: "Telling someone is a coping tool too. It doesn't mean you failed at the others."

### Why it works cards
- What stress is: "Stress is your body's response to new or hard situations. A little can help you rise to a challenge." (CDC)
- Signs: "Stress can show up as trouble sleeping, trouble concentrating, headaches, stomach problems, or feeling worried, angry or sad." (CDC)
- Relaxation response: "Relaxation tools aim to bring on the relaxation response: slower breathing, lower blood pressure and a slower heart rate. It's the opposite of the stress response." (NCCIH)
- Which part each tool works on (the tool's own grouping): Body first: Slow breathing, Tense and release, Shake it out. Attention first: Five senses, Calm place. Thoughts first: Worry dump. People: Talk to someone.
- Testing: "Researchers test ideas by measuring before and after. One try is one data point. A tool that didn't help today might help on another day."

### Help footer (every mode)
One calm line: "Stress that won't let up is worth talking about. A trusted adult or your school counselor can help. In the US, call or text 988." with **More help** (a dialog, Esc or **Close** closes it, focus returns): "988 Suicide & Crisis Lifeline: call or text 988, or chat at 988lifeline.org. Free and confidential, any time, day or night." / "If someone is in immediate danger, call 911." / "This tool is for practice and learning. It can't tell you what you feel or diagnose anything." The link `https://988lifeline.org` opens only when clicked.

## Interactions in detail
- Notebook summary (computed on the page session's tests): change = before minus after (positive is calmer). Lines: with no rated tests, the empty note; with one: "1 test so far. Try more tools, or the same one again, to compare."; otherwise "Moved you most so far: {tool} ({n} tries, about {avg} steps calmer on average)." The average is rounded to the nearest half ("about 1 step", "about 1.5 steps"). Tools tied on the rounded average are all named, each with its tries. If the best rounded average is 0 or less: "No tool moved the gauge much yet. That happens. Some tools work better on a busier day, and talking to someone always counts."
- If the Before pick is 1 (Calm and loose): step 3 adds "You started calm, so there wasn't much room to move. Try this tool on a busier day."
- A change of more wound up is shown plainly, never as failure: "1 step more wound up. Good to know: this one might not be your tool, or not today."
- Stop during step 2 ends the test without the After step; it is not added. Start over restarts the tool's timer. Pause freezes timer, sound and voice.
- My toolkit card: on screen only, in My notebook; it lists starred tools and their how-tos and the help footer text. No ratings, no typed text, no name field, no print and nothing to carry to another device (Cory's scope rule).
- No localStorage at all. Reload clears everything (the note says so).
- Auto-plays: the tools run 60 to 75 s each because the one-minute exercise is the experiment; Pause, Start over and Stop stay live the whole time and act at once.
- Motion off: the dot, the glow, the pose sway and the boat stop moving but every timing stays the same; the breath pace is then shown as a filling bar with "In" and "Out" labels.
- Keyboard: gauge buttons respond to 1 to 5; Space is Follow along in Slow breathing; Esc is Stop.

## Look
- Accent `--brand` #4f6b2c (moss green: quiet, outdoors), on an oatmeal `:root`: paper #f5f3ea, ink #23281c, muted #5f6553, line #dcd8c6, focus #2f5bd3, panel #fffdf6; stage #e7ecdb with the pacer line #5b7a36. Gauge from slate #3f6fa3 to clay #b5562f. Notebook paper #fffdf6 with faint blue rules.
- Contrast: accent on white 6.05:1, on paper 5.44:1; white on accent 6.05:1; ink on paper 13.57:1; muted on paper 5.44:1; ink on stage 12.52:1; muted on stage 5.02:1; pacer line on stage 4.07:1 (graphic); slate on white 5.23:1; clay on white 4.84:1.
- Different from feelings siblings (calm-corner green-teal #2f7a62, mind-map teal #1f5c63, feelings-weather-report #26627a, feelings-faces #b0407a), resilience-map pink, and group siblings (pressure-point berry, relationship-spectrum teal-blue, screen-time-detective blue).

## Art
Local FLUX (`scripts/localart.py`) for every image; no people (the mannequin is a wooden figure with no face or hands detail, not a person). One soft painterly style, asked in one session. Not the same images as resilience-map's island or calm-corner's corner.
- st-toolbox: "An open wooden toolbox seen from slightly above, a wide empty tray inside, worn brass corners, soft painterly style, plain white background"; 4:3; cutout yes; people no; the home focus, tiles sit in the tray.
- st-icons (kit of 7, one shared prompt "a single small object, soft painterly style, plain white background" with): a pinwheel (Slow breathing), a squishy stress ball (Tense and release), a magnifying glass (Five senses), a folded paper note (Worry dump), a pair of sneakers (Shake it out), a postcard with a blank back (Calm place), two mugs side by side (Talk to someone); 1:1; cutout yes; people no; one per tile, all drawn at the same 72 px box.
- st-mannequin (kit of 11, one shared prompt "a plain light wooden artist's mannequin with smooth round joints, soft painterly style, plain white background" with the pose): standing straight facing front (Tense and release); marching with one knee up; arms out making circles; arms down shaking loose; reaching up and leaning to one side; shoulders raised in a roll; sitting on a stool tapping heels; sitting with arms out in circles; sitting with arms down shaking loose; sitting reaching up and leaning; sitting with shoulders raised in a roll; 3:4; cutout yes; people no; one pose per move, swapped on the move change and swayed gently in code; all drawn at one height with the feet (or stool) on the same floor line.
- st-note: "A blank cream paper note card with faint blue lines, a soft shadow, soft painterly style, plain white background"; 4:3; cutout yes; people no; the Worry dump card, the text box drawn on it in code.
- st-boat: "A small folded paper boat made of cream lined paper, soft painterly style, plain white background"; 1:1; cutout yes; people no; swapped in on Fold it up and floated off in code.
- st-beach: "A quiet beach at sunset, gentle waves, warm orange and lilac sky, smooth sand, soft painterly style, full frame"; 16:9; cutout no; people no; Calm place background.
- st-forest: "A forest path just after rain, tall trees, ferns, sunlight through mist, wet leaves shining, soft painterly style, full frame"; 16:9; cutout no; people no; Calm place background.
- st-cabin: "Inside a snug wooden cabin, a window showing falling snow on pine trees, a glowing fireplace and a folded blanket on a chair, soft painterly style, full frame"; 16:9; cutout no; people no; Calm place background.
- st-rooftop: "A city rooftop garden at night with potted plants and string lights, distant lit windows and a few stars, soft painterly style, full frame"; 16:9; cutout no; people no; Calm place background.
25 images, none with people. The breathing hill line, the gauge, the body-area glow, the five senses dots, the notebook page and chart, and the Why it works meters are drawn in code (they are diagrams, charts and controls).

## Voice
`soft-breath` (Enceladus): "Say softly and calmly, like a mindfulness teacher." Different from calm-corner (warm-teacher), resilience-map (easy-coach), comeback-club (upbeat-guide), conflict-coach (big-sister), goal-tracker (easy-coach) and the group siblings (screen-week science-narrator, pressure-point smooth-narrator, relationship-spectrum wise-mentor). Here narration truly helps: students can close their eyes during a tool. `Curio.voice`, `scope: () => state.mode`; Read speaks the hint, or the open card.
| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wTry | how | Try a tool entered, home showing | Tap a tool in the toolbox to start a test. | a tile tapped, or mode left |
| before | how | first Before step | Tap the button that matches how your body feels right now. Or tap Skip rating. | a gauge button or Skip tapped |
| follow | how | first Slow breathing run | To follow along, hold Space or the big button while you breathe in. | tool stopped, paused or finished |
| senses | how | first Five senses run | Tap a dot each time you notice one. Tap Done when you are ready. | tool left |
| worry | how | first Worry dump run | Type what's on your mind in the box. Then tap One small step, or Fold it up. | a button tapped, or tool left |
| place | how | first Calm place picker | Tap a place to go there. | a place tapped |
| after | how | first After step | Now tap how your body feels after. | a gauge button tapped |
| add | how | first change line has played | Tap Add to notebook to keep this test. | Add or Try another tool tapped |
| wBook | how | My notebook entered with at least one test | Your tests show up here. Tap a star in the panel to add a tool to your toolkit. | a star tapped, or mode left |
| wBook0 | how | My notebook entered with no tests | No tests yet. Tap Try a tool at the top to run one. | mode left |
| wWhy | how | Why it works entered | Tap the switch in the panel to see stress and relaxation side by side. | switch tapped, or mode left |
| guide.breath.* | event | first breath of each run: "Breathe in." / "And out, slowly." / "Hold." (later breaths use the tones) | | tool stopped or paused |
| guide.tense.* | event | each area's tense line and "Let it go. Notice the difference." (6 lines) | | tool stopped or area passed |
| guide.senses.* | event | "Notice five things you can see." and the four other rows (5 lines) | | row passed |
| guide.shake.* | event | each move's name line (5 lines) | | move passed |
| guide.place.* | event | the four Calm place prompts | | place left |
| change | event | the step 3 change line, every test | | another test started |
Guide lines use `wait: true` so the timer waits for the line to finish its turn. No line names a control that is hidden or disabled at that moment (add plays only once Add to notebook shows; wBook only when the stars are live).

## Family engine
Feelings family (calm-corner, feelings-faces, feelings-weather-report, mind-map are built; none uses a shared kit file). This tool keeps their shared patterns, written fresh on the kit (`Curio.voice`), and does not add a family file:
- Before and after check-in, never saved (calm-corner's faces and compare line): here the five-step body gauge and the change line.
- Timed calm tools that keep their timing with Motion off (calm-corner's PACE and Calm mode): here every tool timer.
- The help card wording (mind-map, resilience-map): here the footer and More help, same 988 text.
If a later feelings sibling needs the gauge and timers too, move them into `kit/feelings.js` then.

## Sources
- CDC, Coping with stress (Living with mental health): stress definition; signs; "Take deep breaths, stretch, or meditate", "Keep a journal", "Move more", "Talk with people you trust". https://www.cdc.gov/mental-health/living-with/index.html
- NIH NCCIH, Relaxation Techniques: What You Need To Know: relaxation response (slower breathing, lower blood pressure, reduced heart rate); breathing exercises, progressive relaxation, guided imagery. https://www.nccih.nih.gov/health/relaxation-techniques-what-you-need-to-know
- 988 Suicide & Crisis Lifeline: call or text 988, chat at 988lifeline.org, 24/7. https://988lifeline.org (same wording as resilience-map, checked October 2026)
- National Health Education Standards (SHAPE America), Standards 1, 7 and 8.
- Tool's own choices (labeled, not sourced facts): the five gauge steps and their words, the 4-in 6-out and box paces, the 5 s and 10 s tense and release timing, the 60 s routines, the grouping of tools by body, attention, thoughts and people.
- Checks run (Python, `st.py` in the R25 scratch folder): timings 6 x 10 = 60 s, 4 x 16 = 64 s, 5 x 15 = 75 s, 20 + 4 x 10 = 60 s, 4 x 15 = 60 s. Summary rule on test sets: changes 2, 1, 0 for Slow breathing and 1 for Five senses tie at 1.0, so the old Done when check (Slow breathing named alone) was wrong; now tested with 2, 2, 1 and 1 (Slow breathing, 3 tries, about 1.5 steps). One try of +1 among four 0s rounds to 0, so the "much yet" line plays (wording fixed). Mixed +4 and -4 on two tools names the +4 tool. Contrast ratios recomputed: all as listed.

## Done when
1. Every tool runs a full test: Before, the tool for its stated time (60, 64, 75, 60 and 60 s), After, Add to notebook; the notebook row and the dot chart match.
2. Skip rating runs the tool and adds nothing to the notebook; Stop during a tool adds nothing.
3. With changes 2, 2 and 1 for Slow breathing and 1 for Five senses, the summary names Slow breathing, 3 tries, about 1.5 steps calmer; with 1 and 1 on two tools, both are named.
4. Worry dump text is gone from the DOM and memory after Fold it up or Done; nothing appears in localStorage or sessionStorage at any point.
5. The My toolkit card lists only starred tools' names, how-tos and the help text; there is no print or export anywhere.
6. Motion off: no movement, same timings; breathing shows the In and Out bar.
7. Focus: the toolbox on home, the gauge on Before and After, the running tool on Try it, the dot chart in My notebook are each the biggest, central thing at 1366x768 and 680x425.
8. A tap on Pause or Stop while a tool and its guide line are playing acts at once (timer, sound and voice stop within 100 ms).
9. Voice: each how line is spoken once per load and then only updates the hint; guide lines play in step with the timer and are dropped on Pause or Stop; a second run of Slow breathing speaks the first breath's cue again (event) and then uses tones.
10. The help footer and More help show the 988 text exactly as in Content at every size, never covering the Pause and Stop buttons.
11. At 1366x768 and 680x425 the gauge's five buttons and the step strip are visible without scrolling; at 375 wide the toolbox tiles wrap to two columns.
12. All 25 paintings show; the mannequin poses swap on each move and stand on one floor line.

## Open questions
- Keep the 988 line in a 6-8 tool's footer (as in resilience-map), or show only "a trusted adult or your school counselor" and keep 988 inside More help?
- Should students be able to save their starred toolkit (tool names only, no ratings) on the device with a Clear button? This spec saves nothing. Print my toolkit was removed (print cards are out of scope); the toolkit now shows on screen only.
- Shake it out and Tense and release now use a painted wooden mannequin instead of a person, so no image waits on Cory. Fine, or should a real teen demonstrate the moves (people, Gemini)?
- The worry dump asks students to type a real worry, kept in memory and erased. Fine as is, or should it start with an example worry already typed so no one has to write their own?
