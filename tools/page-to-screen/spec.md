# Page to Screen

## One idea
A story can keep a secret that a camera cannot: shoot Saki's "The Open Window" in 15 shots, choosing for each what the audience sees and hears, and the tool keeps two trays filling as you go, **Page only** (sentences no shot of yours carries, like the narrator's dry jokes about Framton) and **Screen only** (things your film must show that Saki never says, like Vera's face while her aunt talks), while a Suspicion line shows when a viewer of your film would start to guess that Vera made the whole thing up; then you say what each medium makes its audience notice.

## Not like
- portrait-in-four-media (ela 10, live or specced): one real life told in four nonfiction forms, compared claim by claim. Here one short story and one film plan, compared by what each can and cannot show.
- page-audio-screen (ela 6 to 8, concept): a book club recommends text, audio or film versions. Here the student makes the film choices and watches the story's secret survive or leak.
- storyboard-studio (arts 9-12, spec): camera placement on a floor plan and the 180-degree rule. Here no camera geometry: each shot is a choice of who is in frame and what is heard, and the measure is what the story loses or gains.
- director-s-chair (arts 9-12, spec): one stage scene in five theater traditions. Here prose into film, and the reader's knowledge is the subject.
- ambiguity-lab (ela 12, this group): changing a story's structure. Here the words stay; the medium changes.

## Who and how
- Grade 10 ELA, module One Story, Two Media: "Compare a subject in two artistic mediums".
- Standards: RL.9-10.7, MA:Re8.
- Driver: students on laptops, alone or in pairs, after reading the story (about 6 minutes; 1,229 words). 25 to 35 minutes. A teacher can project Screen and take votes on each shot.
- tool.json: driver "students", minutes "25-35", modes ["Story", "Shoot", "Screen"] (the first mode was "Read"; renamed so it is never confused with the kit's Read button), grades_label "Grade 10". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Page to Screen", small line "The Open Window, by Saki (1914)"; Motion, Sound, Read. A content line on first open: "A short, funny ghost story. No one is hurt."

**Story.** Focus: the story text, a wide reading column in the middle of the stage; the shot strip is a slim row above it. The whole story, paragraph by paragraph, each sentence a tappable span. A shot strip runs along the top (15 small frames, each a thumbnail of that shot's current composite). Tap a sentence: the shot that carries it lights, or a **Page only** tag shows. Tap a frame: its sentences light in the story.

**Shoot.** Focus: the shot's frame, large on the left (about 60% of the stage width), with its chip rows beside it. One shot at a time: the frame is a painted backdrop (Art) with painted character cutouts placed on it by the chips, and its choices on the right as chip rows (see Content). The frame recomposes as chips change: which backdrop, who is in it, how big (wide, medium and close-up are the same cutouts placed and scaled, or a face cutout for close-ups), and a small speaker icon drawn in code for each sound. Under the frame: **Carries** (the sentences this shot now puts on screen, quoted short) and **Adds** (what the shot shows that the story never says). Back and Next move between shots; a **Use ours** button fills a shot with our choices.

**Screen.** Focus: the playing frame with its subtitle, the largest thing on the stage; the Suspicion line and trays sit below. Plays the film as an animatic: each frame held 3 to 6 seconds, dialogue as subtitles, sound cues as captions in brackets ("[a man's voice, singing]"). A full play runs 45 to 90 seconds; it stays whole because the film in order is the point, and every control stays live: Pause, Back a shot and Next shot act at once, and the Film / Sound only and Yours / Ours switches change the frame on screen immediately, not at the next shot. Two switches: **Film** or **Sound only** (the frames go dark and only the subtitles and captions remain, a radio version), and **Yours** or **Ours**. Under the player:
- the **Suspicion line**: a small stepped line, one step per shot, 0 to 5, "How much would a viewer suspect Vera by now?", computed from the choices;
- the two trays, **Page only** and **Screen only**, with counts;
- the **Emphasis card**: two prompts, "On the page, the reader notices ___ because ___." and "In my film, the viewer notices ___ because ___." (up to 200 characters each, saved).

Panel (right): `#hint`, **Shots set** (n of 15), **Twist kept?** (Yes while the Suspicion line stays at 2 or below until shot 13, else "Leaked at shot n"), and **Clear my work** (asks Yes / No).

## Content
Text: Saki (H. H. Munro), "The Open Window", in Beasts and Super-Beasts (London: John Lane, 1914), quoted whole from Project Gutenberg eBook #269: 29 paragraphs, 1,229 words (counted 2026-10-27, every space-separated token with a letter or digit). Paragraphs are numbered p0 ("My aunt will be down presently, Mr. Nuttel,") to p28 ("Romance at short notice was her speciality."). The dash ending p13 ("walk in through that window--") and the one in p20 ("alert attention--but not") show as two hyphens. Shots, drawings, captions and our choices are written for Curio Class. Suspicion values are the tool's own model, marked so on screen ("our estimate, argue with it").

The 15 shots. Each lists the paragraphs it can carry, its chip rows, and ours (in bold). Suspicion adds are shown after a choice in brackets, from a start of 0. A shot's adds are summed first, then the line is held between 0 and 5 (so shot 4 with a flashback and a Flat voice stays where it was).
1. **Arrival** (p1 to p3). Size: **Wide**, Medium. Framton's thoughts: **Leave out**, Voice-over (carries p1 and p2), Title card. Adds: the house, the season, his face.
2. **The niece** (p0, p4 to p8). Size: Wide, **Medium**. Vera: **Polite**, Bored, Studying him (+1: she is sizing him up). Adds: what Vera looks like; Saki says only "very self-possessed".
3. **The window** (p11, p12). Size: Wide, **Insert of the window**. Sound: **Room tone**, Wind, Music sting (+0). Adds: the color and size of the French window.
4. **The tragedy** (p9, p10, p13). Who we watch: **Vera**, Framton, The window. Flashback: **None**, Show the men crossing the moor (the film shows the lie as if it were true: carries p13's pictures, Suspicion -1), Show the bog (also -1). Vera's voice: **Falters** (carries "falteringly human"), Flat (+1).
5. **The shudder** (p14). Size: **Close-up of Vera**, Two-shot. Her shudder: **Real**, A beat too long (+1).
6. **The aunt arrives** (p14 to p16). Size: **Medium**, Wide (Vera in frame). If Wide, Vera: **Straight face**, A tiny smile (+3), Looks away.
7. **Snipe in the marshes** (p17, p18). Who we watch: **Framton**, Mrs. Sappleton, Vera (+1 unless shot 6 is Wide with Straight face, the one choice that has already shown her face holding still). Mrs. Sappleton's eyes: **Keep straying to the window** (carries p18's last lines), Stay on Framton. Adds: the horror on Framton's face.
8. **The nerve cure** (p19). Framton's speech: **Subtitles only**, With a voice-over of the narrator's joke (carries "tolerably widespread delusion"). Adds: how dull he is to listen to.
9. **"Here they are at last!"** (p20, p21). Size: Medium, **Close-up of Mrs. Sappleton**. Sound: **Her voice only**, Footsteps outside (+0, but the footsteps arrive before the men are seen).
10. **Vera's stare** (p22). Size: **Close-up**, Medium. Her eyes: **Dazed horror** (carries p22), Calm (+3: gives the game away).
11. **Three figures** (p23). Point of view: **Framton's, through the window**, From the lawn. Light: **Deepening twilight**, Bright. Sound: **The song**, Silence, Music sting. Adds: the men's faces and the spaniel.
12. **The retreat** (p24). Size: **Wide, the drive and the gate**, Medium on Framton. Cyclist in the hedge: **Show it**, Leave out (Page only). Tone: **Comic**, Frightening.
13. **Muddy but dry** (p25, p26). Size: **Medium**. Who we watch: **The husband and Mrs. Sappleton**, Vera.
14. **The spaniel story** (p27). Who we watch: **Vera, calm**, A flashback of the dogs and the grave (carries p27's pictures). Suspicion jumps to 5 here in every version: the film and the story both reveal the trick in this shot.
15. **The last line** (p28). Choices: **Hold on Vera's face, a small smile**, Narrator voice-over, Title card, Cut it (the line goes to Page only).

Examples of sentences that land in Page only: p1's "Privately he doubted more than ever..." unless shot 1 has Voice-over; Framton wondering about "the nice division" (p3) unless shot 1 has Voice-over; "somehow in this restful country spot tragedies seemed out of place" (p10, his thought, never carried); "It was certainly an unfortunate coincidence..." (p18, the narrator's irony) unless shot 8 has Voice-over. Lines an actor can play, such as "He made the last statement in a tone of distinct regret." (p6), are carried by the shot that holds them. The builder lists every sentence's carrying condition in `tools/page-to-screen/shots.json` from this table.

Screen only, filled from choices: Vera's age and face (shot 2), the window's look (3), Vera's face during the aunt's talk (6, only if Wide), the men's faces (11), music (any sting), the cyclist's face (12).

Our film ("Ours"): every bold choice. Its Suspicion line: 0 through shot 13, then 5 at shots 14 and 15. Ours holds on Vera's small smile for the last line, so p28 is shown, not said; the narrator's jokes in p1, p3, p10, p18 and p19 stay in Page only. The builder computes Ours' Page only count from shots.json and the Done when check uses that number.

## Interactions in detail
- Story: sentences are spans with `tabindex`; Enter lights the carrying shot. Tapping a frame scrolls the story to its first sentence.
- Shoot: chip rows are radio groups (arrow keys move, Enter picks); choosing a chip redraws the frame in under 100 ms, updates Carries and Adds, and updates both trays. A shot counts as set once any chip in it is chosen or Use ours is pressed.
- Screen: Play, Pause, Back a shot, Next shot; with Motion off frames cut without a fade. Subtitles are the story's own dialogue, exact. In Sound only the frame area shows a dark panel and the caption in large type.
- Suspicion line: steps drawn in the accent; shot numbers on x; a dotted line for Ours when Yours is shown. Screen readers hear "Shot 6, suspicion 2 of 5".
- Twist kept? updates live.
- A tap during a frame fade or the animatic acts at once: the fade jumps to its end, and any line about the old state is dropped.
- Store: localStorage `p2s-work` (choices, Emphasis card), try/catch. Clear my work (after Yes) empties it.
- Sizes: at 1366x768 and 1280x720 Shoot shows frame and chips side by side; at 680x425 the chips sit under the frame and the story in Story scrolls inside its box; at 760 and 375 wide the shot strip scrolls sideways and chip rows wrap.

## Look
- `kit:theme-912` dark, accent `--brand #7cc4ff` (non-photo blue, the storyboard pencil: frame borders, chips, the Suspicion line, buttons), `--btn #7cc4ff`, brand text on brand `--brand-ink #1c1203`.
- Frames: painted in one pencil-and-wash storyboard style, cool blue-grey washes with warm lamplight, so the frames feel like a storyboard and the pencil-blue accent ties them together. Frame borders and shot numbers in code, ink `#c8d3e0` on `#1a2330`. In wide shots Vera's cutout gets a 2 px accent outline so a student can spot her.
- Trays: Page only marked with a book icon, Screen only with a camera icon; text on `--sec-bg`.
- Neighbors: ambiguity-lab periwinkle (this group, dE 17), portrait-in-four-media coral, storyboard-studio. Nearest catalog color: `--gr-1` (dE 18).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 10.02:1, on panel 9.23:1, on sec-bg 8.75:1; brand-ink on brand 9.85:1; frame ink `#c8d3e0` on `#1a2330` 10.44:1. All pass AA.

## Art
One pencil-and-wash storyboard style for every image: backdrops by local FLUX (`scripts/localart.py`), people by Gemini (`scripts/art.py`), every person reviewed by Cory. People are kept because what each face shows (or hides) is the lesson; everything else is a place. Text (subtitles, captions, shot numbers) stays in code.

Backdrops (local FLUX, full frame, empty of people; 16:9; cutout no; people no):
- house-exterior: "A quiet English country house in October, ivy on old brick, a gravel drive and a lawn, late afternoon, pencil and wash storyboard painting"; shot 1.
- drawing-room: "An Edwardian country-house drawing room with armchairs, a small table and a fireplace, a large French window standing open onto a lawn, late afternoon light, empty, pencil and wash storyboard painting"; shots 2, 4 to 10, 13 to 15.
- window-insert: "A tall French window standing wide open onto a lawn, close view, October afternoon, pencil and wash storyboard painting"; shot 3.
- lawn-twilight: "A lawn seen through an open French window at deepening twilight, a path leading toward the window, empty, pencil and wash storyboard painting"; shot 11 (Deepening twilight).
- lawn-bright: the same view in bright afternoon light; shot 11 (Bright).
- drive-gate: "A gravel drive leading to an open iron gate in a tall hedge, a country road beyond, dusk, empty, pencil and wash storyboard painting"; shot 12.
- moor: "A wide wet moor with dark heather under a low grey sky, empty, pencil and wash storyboard painting"; shot 4, the men crossing the moor.
- bog: "A treacherous bog with black pools and reeds on a misty moor, empty, pencil and wash storyboard painting"; shot 4, the bog.
- river-night: "A riverbank at night under a pale moon, a freshly dug pit in the earth, a pack of thin wild dogs snarling at its edge, pencil and wash storyboard painting"; shot 14's flashback.

People (Gemini, all `people: true`, cutouts on a plain white background, one shared prompt: "<figure>, Edwardian clothes, pencil and wash storyboard painting, plain white background"):
- vera-seated (kit of 3; 3:4): "a self-possessed fifteen-year-old girl seated upright in an armchair" with a straight face / with a tiny knowing smile / looking away toward the window; wide and medium shots 2, 6, 7, 13.
- vera-face (kit of 6; 1:1, head and shoulders): the same girl, polite and attentive / bored / studying the visitor closely / faltering, sad / a tiny knowing smile / dazed horror, eyes wide; close-ups and mediums in shots 2, 4, 5, 10, 14 (polite also stands for calm) and 15.
- framton-seated (3:4): "a nervous, thin young man in a tweed suit perched on the edge of an armchair"; shots 1, 2, 7, 8.
- framton-horror (1:1): the same man, head and shoulders, frozen in horror; shot 7.
- framton-fleeing (3:4): the same man running headlong, full figure; shot 12.
- aunt-talking (3:4): "a brisk, cheerful middle-aged woman standing and talking"; shots 6, 7, 9, 13.
- aunt-window (1:1): the same woman, head and shoulders, glancing past the viewer toward a window; shot 9.
- hunters-spaniel (4:3): "three men in shooting clothes carrying guns, one with a white waterproof coat over his shoulders, with a brown spaniel at their heels, walking toward the viewer, full figures"; shots 4 (on the moor), 11, 13.
- cyclist (4:3): "a man on a bicycle swerving into a hedge"; shot 12, only when Show it is chosen.
25 images: 9 without people (FLUX) and 16 with people (Gemini, waiting on Cory). Drawn in code: frame borders, speaker icons, subtitles, captions, the Suspicion line, trays and icons. preview.svg: three frames in a strip built from drawing-room, window-insert and lawn-twilight, with no person in it.

## Voice
Bank voice `friendly-dad` (Achird), style "Say warmly and easily, like a film club host introducing tonight's picture". Not used by any neighbor or another tool in this batch. `Curio.voice`, scope the mode. The story is never voiced; Read speaks the hint. Event line ids: wide, leak.
- welcome (how, first open; stale when a mode is tapped): "One short story, fifteen shots. Tap Story to read it, or tap Shoot to start filming."
- story (how, first Story; stale when a sentence or frame is tapped): "Tap a sentence to see which shot carries it. Some sentences won't fit in any shot."
- shoot (how, first Shoot; stale when a chip is tapped): "Tap a chip in each row. Watch what lands in Page only and Screen only."
- wide (event, shot 6 set to Wide; stale on leaving shot 6 or changing its size): "In a wide shot Vera's in the room. Saki never says what her face is doing. You have to."
- leak (event, Twist kept? turns to Leaked; stale when it turns back): "Careful. A viewer might guess the trick at shot {n}."
- screen (how, first Screen; stale when Play is tapped): "Here's your film. Tap Play. Then try Sound only, and fill in what each version makes you notice."
- Read speaks the hint, which names the next control (a sentence, a chip, Next, Play, the Emphasis card).

## Family engine
none

## Sources
- Saki (H. H. Munro), "The Open Window," in Beasts and Super-Beasts (London: John Lane, 1914), Project Gutenberg eBook #269, https://www.gutenberg.org/ebooks/269 ; paragraph count and word count computed from that file on 2026-10-27.
- Saki's life and the story's place in his work: Britannica, "Saki," https://www.britannica.com/biography/Saki
- Shot scale names, point-of-view shots, inserts and voice-over: David Bordwell, Kristin Thompson and Jeff Smith, Film Art: An Introduction, 12th ed. (McGraw-Hill, 2019), ch. 5 "The Shot: Cinematography" and ch. 7 "Sound in the Cinema" (as cited in storyboard-studio).
- Standards: CCSS ELA RL.9-10.7, https://www.thecorestandards.org/ELA-Literacy/RL/9-10/ ; NCAS Media Arts MA:Re8, https://www.nationalartsstandards.org/
- Shots, captions, our choices and Suspicion values: written for Curio Class.
- Checks run (Python, 2026-10-29): every combination of the eight Suspicion chip rows (1,296) run through the model. Ours: 0 through shot 13, then 5 at 14 and 15; Twist kept? Yes. Shot 6 Wide with A tiny smile: 3 from shot 6, "Leaked at shot 6". Studying him then a flashback: 1 after shot 2, back to 0 at shot 4. A flashback at 0 stays 0. Three +1 choices (Studying him, Flat, A beat too long) leak at shot 5. The highest value before shot 14 is 5 (capped). The old text left the order of a flashback (-1) and a Flat voice (+1) inside shot 4 open, which changed the result at 0, so a shot's adds are now summed before the 0 to 5 hold. Animatic: 15 frames at 3 to 6 s is 45 to 90 s (reason in Screen). Contrast ratios in Look recomputed with the WCAG 2.1 formula; all match to 0.01.

## Done when
1. Story shows all 29 paragraphs word for word from eBook #269 (1,229 words by the stated rule), with "--" for the two dashes.
2. With Ours, the Suspicion line is 0 through shot 13 and 5 at shot 14, and Twist kept? says Yes.
3. Setting shot 6 to Wide with A tiny smile makes Twist kept? read "Leaked at shot 6".
4. Setting shot 1 to Voice-over moves p1 and p2 out of Page only; setting shot 15 to Cut it moves p28 in.
5. Shot 4's flashback chips add "the men crossing the moor" (or "the bog") to Screen only, and lower Suspicion by 1 when it is above 0 (for example after shot 2's Studying him).
6. Screen plays all 15 frames with exact subtitles; Sound only hides frames and keeps captions; Motion off cuts without fades.
7. Reload keeps choices and the Emphasis card; Clear my work (after Yes) empties them; no network; console clean.
8. At every size in STANDARDS.md the frame and its chips are reachable without page scroll; 375 wide works in `drive.py --host`.
9. Focus: at 1366x768 and 680x425 the frame is the largest thing in Shoot and in Screen; in Story the text column is.
10. Tap while it plays: Pause, Back a shot, Next shot and both switches act at once during the animatic, and a chip tapped during a fade recomposes the frame at once.
11. Every chip that changes who is in frame or how big changes the painted composite: Wide shot 6 shows vera-seated beside aunt-talking; Close-up shot 10 shows the chosen vera-face.

## Open questions
- [page-to-screen] The frames now ask for 16 painted people (Vera 9, Framton 3, Mrs. Sappleton 2, the hunters 1, the cyclist 1), all Gemini and all waiting on Cory. Paint the cast, or keep the people as simple drawn figures over the painted rooms?
- [page-to-screen] The Suspicion numbers are our own estimate of a viewer's reaction, labeled "our estimate, argue with it." Is a made-up meter acceptable here, or should the tool only show the trays?
- [page-to-screen] The spaniel story mentions a night spent in "a newly dug grave" with snarling dogs (p27, a lie Vera tells). Mild, but a parent might want to see it first.
