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
- tool.json: driver "students", minutes "25-35", modes ["Read", "Shoot", "Screen"], grades_label "Grade 10". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Page to Screen", small line "The Open Window, by Saki (1914)"; Motion, Sound, Read. A content line on first open: "A short, funny ghost story. No one is hurt."

**Read.** The whole story, paragraph by paragraph, each sentence a tappable span. A shot strip runs along the top (15 small drawn frames). Tap a sentence: the shot that carries it lights, or a **Page only** tag shows. Tap a frame: its sentences light in the story.

**Shoot.** One shot at a time, large: the drawn frame on the left (a simple flat drawing of the drawing room, the French window, the lawn), and its choices on the right as chip rows (see Content). The frame redraws as chips change: who is in it, how big, a small speaker icon for each sound. Under the frame: **Carries** (the sentences this shot now puts on screen, quoted short) and **Adds** (what the shot shows that the story never says). Back and Next move between shots; a **Use ours** button fills a shot with our choices.

**Screen.** Plays the film as an animatic: each frame held 3 to 6 seconds, dialogue as subtitles, sound cues as captions in brackets ("[a man's voice, singing]"). Two switches: **Film** or **Sound only** (the frames go dark and only the subtitles and captions remain, a radio version), and **Yours** or **Ours**. Under the player:
- the **Suspicion line**: a small stepped line, one step per shot, 0 to 5, "How much would a viewer suspect Vera by now?", computed from the choices;
- the two trays, **Page only** and **Screen only**, with counts;
- the **Emphasis card**: two prompts, "On the page, the reader notices ___ because ___." and "In my film, the viewer notices ___ because ___." (up to 200 characters each, saved).

Panel (right): `#hint`, **Shots set** (n of 15), **Twist kept?** (Yes while the Suspicion line stays at 2 or below until shot 13, else "Leaked at shot n"), and **Clear my work** (asks Yes / No).

## Content
Text: Saki (H. H. Munro), "The Open Window", in Beasts and Super-Beasts (London: John Lane, 1914), quoted whole from Project Gutenberg eBook #269: 29 paragraphs, 1,229 words (counted 2026-10-27, every space-separated token with a letter or digit). Paragraphs are numbered p0 ("My aunt will be down presently, Mr. Nuttel,") to p28 ("Romance at short notice was her speciality."). The dash ending p13 ("walk in through that window--") and the one in p20 ("alert attention--but not") show as two hyphens. Shots, drawings, captions and our choices are written for Curio Class. Suspicion values are the tool's own model, marked so on screen ("our estimate, argue with it").

The 15 shots. Each lists the paragraphs it can carry, its chip rows, and ours (in bold). Suspicion adds are shown after a choice in brackets, from a start of 0; the line never drops below 0 or goes above 5.
1. **Arrival** (p1 to p3). Size: **Wide**, Medium. Framton's thoughts: **Leave out**, Voice-over (carries p1 and p2), Title card. Adds: the house, the season, his face.
2. **The niece** (p0, p4 to p8). Size: Wide, **Medium**. Vera: **Polite**, Bored, Studying him (+1: she is sizing him up). Adds: what Vera looks like; Saki says only "very self-possessed".
3. **The window** (p11, p12). Size: Wide, **Insert of the window**. Sound: **Room tone**, Wind, Music sting (+0). Adds: the color and size of the French window.
4. **The tragedy** (p9, p10, p13). Who we watch: **Vera**, Framton, The window. Flashback: **None**, Show the men crossing the moor (the film shows the lie as if it were true: carries p13's pictures, Suspicion -1), Show the bog (also -1). Vera's voice: **Falters** (carries "falteringly human"), Flat (+1).
5. **The shudder** (p14). Size: **Close-up of Vera**, Two-shot. Her shudder: **Real**, A beat too long (+1).
6. **The aunt arrives** (p14 to p16). Size: **Medium**, Wide (Vera in frame). If Wide, Vera: **Straight face**, A tiny smile (+3), Looks away.
7. **Snipe in the marshes** (p17, p18). Who we watch: **Framton**, Mrs. Sappleton, Vera (+1 unless Straight face). Mrs. Sappleton's eyes: **Keep straying to the window** (carries p18's last lines), Stay on Framton. Adds: the horror on Framton's face.
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
- Read: sentences are spans with `tabindex`; Enter lights the carrying shot. Tapping a frame scrolls the story to its first sentence.
- Shoot: chip rows are radio groups (arrow keys move, Enter picks); choosing a chip redraws the frame in under 100 ms, updates Carries and Adds, and updates both trays. A shot counts as set once any chip in it is chosen or Use ours is pressed.
- Screen: Play, Pause, Back a shot, Next shot; with Motion off frames cut without a fade. Subtitles are the story's own dialogue, exact. In Sound only the frame area shows a dark panel and the caption in large type.
- Suspicion line: steps drawn in the accent; shot numbers on x; a dotted line for Ours when Yours is shown. Screen readers hear "Shot 6, suspicion 2 of 5".
- Twist kept? updates live.
- Store: localStorage `p2s-work` (choices, Emphasis card), try/catch. Clear my work (after Yes) empties it.
- Sizes: at 1366x768 and 1280x720 Shoot shows frame and chips side by side; at 680x425 the chips sit under the frame and the story in Read scrolls inside its box; at 760 and 375 wide the shot strip scrolls sideways and chip rows wrap.

## Look
- `kit:theme-912` dark, accent `--brand #7cc4ff` (non-photo blue, the storyboard pencil: frame borders, chips, the Suspicion line, buttons), `--btn #7cc4ff`, brand text on brand `--brand-ink #1c1203`.
- Frames: flat drawings in a pencil style, ink lines `#c8d3e0` on `#1a2330`, figures as simple shapes with faces only in close-ups; Vera always in the accent outline so a student can spot her in a wide shot.
- Trays: Page only marked with a book icon, Screen only with a camera icon; text on `--sec-bg`.
- Neighbors: ambiguity-lab periwinkle (this group, dE 17), portrait-in-four-media coral, storyboard-studio. Nearest catalog color: `--gr-1` (dE 18).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 10.02:1, on panel 9.23:1, on sec-bg 8.75:1; brand-ink on brand 9.85:1; frame ink `#c8d3e0` on `#1a2330` 10.44:1. All pass AA.

## Art
None from a museum. The 15 frames, icons and preview.svg (three frames in a strip, the middle one a close-up of a girl's calm face beside an open window) are drawn in code; no outside images.

## Voice
Bank voice `friendly-dad` (Achird), style "Say warmly and easily, like a film club host introducing tonight's picture". Not used by any 9-12 ELA tool or this group. `Curio.voice`, scope the mode. The story is never voiced; Read speaks the hint.
- welcome (how, first open): "One short story, fifteen shots. You decide what the camera sees."
- read (how, first Read): "Tap a sentence to see which shot carries it. Some sentences won't fit in any shot."
- shoot (how, first Shoot): "Pick a chip in each row. Watch what lands in Page only and Screen only."
- wide (event, shot 6 set to Wide; stale on leaving shot 6): "In a wide shot Vera's in the room. Saki never says what her face is doing. You have to."
- leak (event, Twist kept? turns to Leaked; stale when it turns back): "Careful. A viewer might guess the trick at shot {n}."
- screen (how, first Screen): "Here's your film. Try Sound only, then fill in what each version makes you notice."

## Family engine
none

## Sources
- Saki (H. H. Munro), "The Open Window," in Beasts and Super-Beasts (London: John Lane, 1914), Project Gutenberg eBook #269, https://www.gutenberg.org/ebooks/269 ; paragraph count and word count computed from that file on 2026-10-27.
- Saki's life and the story's place in his work: Britannica, "Saki," https://www.britannica.com/biography/Saki
- Shot scale names, point-of-view shots, inserts and voice-over: David Bordwell, Kristin Thompson and Jeff Smith, Film Art: An Introduction, 12th ed. (McGraw-Hill, 2019), ch. 5 "The Shot: Cinematography" and ch. 7 "Sound in the Cinema" (as cited in storyboard-studio).
- Standards: CCSS ELA RL.9-10.7, https://www.thecorestandards.org/ELA-Literacy/RL/9-10/ ; NCAS Media Arts MA:Re8, https://www.nationalartsstandards.org/
- Shots, drawings, captions, our choices and Suspicion values: written for Curio Class.

## Done when
1. Read shows all 29 paragraphs word for word from eBook #269 (1,229 words by the stated rule), with "--" for the two dashes.
2. With Ours, the Suspicion line is 0 through shot 13 and 5 at shot 14, and Twist kept? says Yes.
3. Setting shot 6 to Wide with A tiny smile makes Twist kept? read "Leaked at shot 6".
4. Setting shot 1 to Voice-over moves p1 and p2 out of Page only; setting shot 15 to Cut it moves p28 in.
5. Shot 4's flashback chips add "the men crossing the moor" (or "the bog") to Screen only, and lower Suspicion by 1 when it is above 0 (for example after shot 2's Studying him).
6. Screen plays all 15 frames with exact subtitles; Sound only hides frames and keeps captions; Motion off cuts without fades.
7. Reload keeps choices and the Emphasis card; Clear my work (after Yes) empties them; no network; console clean.
8. At every size in STANDARDS.md the frame and its chips are reachable without page scroll; 375 wide works in `drive.py --host`.

## Open questions
- [page-to-screen] The Suspicion numbers are our own estimate of a viewer's reaction, labeled "our estimate, argue with it." Is a made-up meter acceptable here, or should the tool only show the trays?
- [page-to-screen] The spaniel story mentions a night spent in "a newly dug grave" with snarling dogs (p27, a lie Vera tells). Mild, but a parent might want to see it first.
