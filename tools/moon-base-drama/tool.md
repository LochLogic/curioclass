# Moon Base Drama: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: moon-base-drama

#### Built
- Teacher-led K-2 drama with Crew and Mission modes, six painted job badges, eight story beats and three resource choices.
- Ada's readable script card, separate Mission Control narration, radio crackle and captions, story map, Back and Rewind.
- Branch changes restore earlier resources, preserve faded old choices, and change the night greenhouse ending.
- Painted lunar scenes, rover arrival, floating ice, charging battery, warmth feedback, lamp glow and a drooping painted leaf layer.
- Required source, draft metadata with stage built, teacher notes, 33-line voice manifest, audit states, art prompts and handoff are present.
- Final offline bundle: 1,555,762 bytes, about 1,519.3 KiB. Build only; no commits, branch operations or polish round.
- Working directory verified as S:/CurioClass-codex. Project writes stayed in this tool and its Scratch folder.

#### Numbers check
Recomputed in `_scratch/moon-base-drama/setup.py`; results are in `numbers.json`.
- 29.5 / 2 = 14.75 Earth days: about two weeks each of daylight and night.
- 1.62 / 9.81 = 0.1651376, close to one sixth, 0.1666667.
- Spec correction: minus 130 Celsius converts to minus 202 Fahrenheit, not minus 208. No exact temperature occurs in the radio script.
- Contrast: white/brand 9.08, brand/paper 8.17, ink/paper 14.92, muted/paper 6.00, ink/Ada card 15.63.
- Every path was recomputed independently, then played through with held clicks and compared by `verify.py`.

| Path | Light, Water, Warm | Ending |
|---|---|---|
| AAA | 3, 3, 3 | Glowing |
| AAB | 3, 3, 1 | Two full |
| ABA | 3, 2, 3 | Two full |
| ABB | 3, 2, 1 | Droopy |
| BAA | 1, 3, 3 | Two full |
| BAB | 1, 3, 1 | Droopy |
| BBA | 1, 2, 3 | Droopy |
| BBB | 1, 2, 1 | Droopy |

The supplied freezer claim is overbroad for laboratory cryogenic equipment. Exact dialogue is retained; notes explain the home-freezer comparison.

#### Feel check
Played complete perfect and imperfect missions, all three rewind destinations, and a keyboard-only complete mission.
- Best moment: arriving at the greenhouse after changing the story, with the crew's own map icons, three full meters and glowing lamps.
- Flattest moment 1: the first ending differed mainly in words. Added a separately painted planter with code-controlled leaf droop and count-dependent lamps.
- Flattest moment 2: choices initially changed only dots. Added charging and warmth/air-loss feedback, and moved the rover clear of the choices.
- Props visibly grow on assignment; the radio responds immediately. Teacher-controlled pacing leaves room for spoken answers and mime.
- This sustains a class drama through their performances and revisions. Clicking through alone is much shorter than the intended 20 to 30 minutes.
- Bundled bar copies in Scratch and opened Snowy Mail Route and Beat Lab before implementation.
- Looked at `feel-compare.jpg`: Moon Base Drama beside Snowy Mail Route. The painted setting, foreground plants and practical lights meet the visual bar.

#### Done when
1. PASS: 1366x768 and 680x425 frames show a full painted stage, readable Ada card and large on-scene choices. Compact text stays at least 10 px.
2. PASS: all eight held-click path runs reached the calculated ending. Beat 2 has 1, 1, 1; individual resource results match the table.
3. PASS: real Rewind taps at Batteries, Water and Warmth restored 1/1/1, 3/1/1 and 3/3/1. Old later icons fade; active choices are invalidated.
4. PASS for speech content: all beat and result events start through Curio.voice; Radio again repeats the current radio message. Ada's lines are absent from the voice table.
5. PASS: held clicks and the Read/result/Radio again/Back interruption run cut current speech and act. Stale queued lines do not follow the new beat.
6. PASS: Next is disabled only while a choice awaits an answer. At the ending it becomes New mission. No waiting hint names a disabled Next.
7. PASS: audit's five held clicks at two-second intervals were clean for every tested speaking control. A complete run heard the Next how-to once.
8. PASS: audit found no undersized targets or off-screen main controls across every required viewport and state. Repaired compact hints were checked separately.
9. PASS: Motion off returned no active animations in the targeted run; the audit found no infinite animation. Night, meters and objects settle immediately.
10. FAIL literally for no storage: the required shared kit remembers only Motion. PASS for no story storage or tool network requests. No class data is collected.

#### Wave lessons
- Hint and voice: PASS. Hint updates synchronously from state; Read follows the spec's current Mission Control message, or Crew hint. V.heard chooses how-to lines.
- Focus and layout: PASS after repair. Stable button DOM; no focus on load. Back to Crew now focuses its visible tab, checked with held input.
- Sizes: PASS after repair. Every STANDARDS size covered, including 375 in an iframe. Compact hints now occupy visible space beside the radio or in the phone bar.
- No giveaways: PASS within this drama. No extra correct marks precede a choice. The supplied science facts and choice order remain as specified.
- Honest numbers: PASS. Dots are story resources, with three meaning full; notes explain that they are not engineering measurements.
- Standards: PASS in the teacher-led format. Children speak and mime roles, revise a branch, and answer Ada's question about its effect using moon science.
- Motion off: PASS. Explicit calm styles stop loops and transitions; audit and targeted animation inspection agree.
- Short choice sets: PASS. All six badges, both answer buttons and the three large rewind options are visible together in their respective states.
- Resize mid-animation: PASS. Audit flipped every listed state and walk action between 1366 and 760 widths without exceptions or stuck controls.
- Late welcome: PASS by supplied behavior. A job or Mission tap gets its own line; no stale Crew welcome follows it.
- Unknown shown as unknown: PASS. Future and old map nodes fade; unmade choices do not contribute resources.
- One look, one meaning: PASS. Job checks mean assigned, filled dots mean resources, and diamonds mean story choices.
- Badge says what is true: PASS. Assigned jobs stay checked; resource dots are derived from active choices, not accumulated taps.
- Hint changes back: PASS. Back, mode changes and rewinds recompute the hint immediately; the voice helper cannot overwrite it later.
- No answer by copying: PASS for this scope. This is a fact-informed role play, not a hidden-clue diagnosis quiz; exact supplied teaching lines remain.

#### Audit leads
Full audit ran once, last after the main build checks: exit 0 in 1,384 seconds, with 22 leads.
Input is preserved as `_scratch/moon-base-drama/audited-bundle.html`; output is `_scratch/moon-base-drama/audit/audit.md`.
- Four default-size hint leads, 680, 800, 1000 and 375: fixed. Hint is visible in compact landscape and in the phone's control bar.
- Seven state hint leads, Mission entry, crew-checked, batteries, water-result, rewind-open, night and card-hidden: fixed by the same state-independent layout repair.
- One rewind keep-region lead: corrected audit configuration. A native modal intentionally covers and makes background controls inert; its own dialog is the keep region.
- Seven welcome leads, Mission and each of six jobs: intentional. The spec makes the Crew welcome stale on a badge tap; Mission opens its own event immediately.
- One Back focus lead: fixed. Back at beat 1 transfers focus to the visible Crew tab. Final held-click check returned focus m-crew.
- Two quick-tap welcome cuts, Crew and Motion: intentional. Every tap must hush speech; the kit marks a welcome heard when it starts. The full welcome caption remains visible.
- Audit had no console errors, undersized targets, resize exceptions, stuck disabled controls or infinite calm animation. Its five-click repeat checks were clean.
The full audit was not rerun after the hint, Back focus, rover placement and keep-region repairs. Targeted checks below cover those changes.
An initial phone host favicon 404 was in the test wrapper, not the tool; a data favicon fixed it. Subsequent phone batches had zero errors.

#### Frames looked at
All paths below are under `_scratch/moon-base-drama/`.
- `bar-frames/`: both bar tools, individually.
- `early-frames/` and `early-fixed/`: compact Crew/Mission and 1366 Crew during construction.
- `size-frames/`: all 11 frames covering 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
- `path-frames/`: all eight endings, Rewind, Back undo, Motion off and grayscale, individually.
- `voice-frames/` and `final-frames/`: held narration, keyboard, battery, warmth, air choice, ice, endings and interruptions.
- `phone-frames/`: final Crew, choice, night, map and water at 375x812 in the iframe host, individually.
- `hint-frames/`, `branch-frames/` and `postfix-frames/`: compact repairs, Back focus, all rewind destinations, retained jobs and fully arrived rover.
- All 65 audit PNGs inspected through eight labeled sheets in `audit-sheets/`; matching critical layouts also inspected as full-size drive frames.
- Every final WebP inspected, including keyed prop edges. `feel-compare.jpg` inspected beside the bar frame.

#### Art made
- 14 images: five settings, six job props, rover, ice block and the additional foreground planter. All have no people.
- Total WebP art: 1,117,298 bytes, about 1,091.1 KiB. Final bundle: about 1,519.3 KiB, below 2 MB.
- Built-in image tool; full prompt set in `art/prompts.json`, raw originals in `art/raw/`, final assets in `art/*.webp`.
- No redraws required. Rekeyed cutouts with hole removal and despill after seeing a green rover fringe. Added the planter to replace the plain code leaf art.
- Generated-image credit is in source, notes and tool.draft.json. Every painted asset is used.

#### Art still to paint
None. Empty hanging suits are equipment; no people, faces or body parts were generated.

#### Engine changes wanted
- `kit/curio.js`, init Motion handler: allow an in-memory-only preference for tools whose spec requires no storage.
- `kit/curio.js`, voice and speakOne: expose playback start/end callbacks for consistent radio glow and crackle with future recorded clips.
No engine files were changed.

#### Left open
- No narration was recorded, as instructed. The manifest requests firm-captain / Alnilam, but current playback uses browser speech; that timbre and audible classroom quality remain unverified.
- Literal no-storage compliance needs the kit option above. Only its shared Motion preference is persisted.
- The exact supplied freezer line remains scientifically overbroad; teacher notes qualify it. The owner can revise the script in the next review.
- Final targeted repairs have not had a second full audit. A cold review is the next workflow step.
- Temporary host.html removed. All test Chrome processes and servers started for this build are closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: moon-base-drama

#### Played

Cold K-2 crew/teacher walk before opening builder reports or source: all weak choices, ending, then a changed battery branch. Strong painted base and props; the class performance makes this a drama.
One review pass, scoped fixes and targeted rechecks. Root verified as `S:\CurioClass-codex`; no commits.

#### Findings fixed

- **blocker, general, entry:** Mission bypassed the disabled Start mission with no assigned job. Both entry routes now require a job; premature Mission taps name and focus the badges.
- **blocker, general, Mission:** trying both answers replaced a poor choice for free; helpful options were always leftmost. Choices now commit until Back/Rewind, with positions varied per mission. Repeated taps never add resources.
- **should fix, general, phone:** the beat label covered battery art and Ada's card hid the changing planter. Moved both existing art layers into clear scene space; verified with real held clicks at 375 px in the host iframe. A follow-up also separated the longest first-beat caption from Ada's card; final measured gap is 3.625 px.
- **should fix, general, voice:** the two-second main path dropped every how-to behind long story lines. The first instruction now leads its event transmission once. Later events repeat without the prefix; log and real speech use the same text.
- **should fix, general, science:** corrected the universal freezer claim to a home freezer, clarified daylight versus a full lunar day and no breathable air versus an exosphere. Spec untouched; notes explain simplifications.
- **should fix, general, compact Mission:** response art disappeared below 640 px height. Restored the existing battery and warmth/air SVGs in clear scene space, retaining paintings and 60 px controls.
- **should fix, general, map:** Read referred to a covered beat and was inaccessible inside the modal. Read map speaks the map instruction. New mission from the modal now focuses visible Next.
- **polish, general, water:** the same rover appeared before/after the answer while only dots changed. It now arrives with ice after the answer, with a smaller late load. The partial-water result explains why the tank stays low.
- **polish, general, crater:** sunlit ice weakened the permanent-shadow lesson. Redrew the existing painting, then made one targeted visibility revision. All deposits are in shadow; rich painted style preserved.
- **polish, general, ending:** the first ending's hint assumed a revision. It now asks which choice helped and names Rewind.

#### Findings left

No remaining blocker or should-fix within this tool's authorized scope. Recording and shared-kit limitations are under Left open. The separate narration recording stage remains outside this brief.

#### Break it

There is no score, quiz, reflection completion gate, best score or saved achievement. Meters are explicitly fictional resources, not knowledge scores or engineering measurements.
Before fixes: repeated taps did not stack dots, but both-option sweeping could replace a weak choice, and all-left reliably filled every meter.
After fixes, real input: five wrong/right alternations per meter stayed at 1/1/1, 3/2/1 and 3/3/1 respectively; all-left gave 1/2/3 and a low ending. Rewind restored 1/1/1, 3/1/1 and 3/3/1; New mission kept jobs and focused Next. Eight final held-click paths match the independent outcomes below. Empty Start and the Mission-tab bypass both remain on Crew after the gate repair; unanswered Next remains at beat 3. Keyboard-only input reached beat 8.
Independent eight-path computation: AAA 333, AAB 331, ABA 323, ABB 321, BAA 133, BAB 131, BBA 123, BBB 121. One full ending, three two-full endings, four low endings.
Production logic also passed 62 DOM-stub checks: every meter's five alternating attempts, eight endings, Back, all rewind targets and eight observed order variants. This supplements browser evidence.
Guessing can succeed by chance in a two-choice drama. Rewind deliberately supports revision; no screen claims that a glowing greenhouse proves mastery. The supplied facts scaffold the crew's choices; children give their reason aloud.

#### Voice walk

Sound on, defaults, held clicks two seconds apart: job, Start, Next twice, weak battery, Next, weak water, Next twice, weak warmth, Next twice, Rewind, Batteries, helpful battery.
Started in order: ready+job, beat 1, Next-how+beat 2, choose-how+beat 3, battery result, beat 4, water result, beat 5, beat 6, warmth result, beat 7, reflection+low ending, map-how, rewind-how+batteries, revised battery result.
`voice-main.json`: no dropped queued lines. Deliberate taps cut long speech immediately as required. Ada's script is never spoken.

| Line/function | Expected | Observed |
|---|---:|---:|
| Start, Next, choose, reflection, map, first rewind how | 1 each | 1 each |
| Job event across five taps | 5 | 5 |
| Choice result across five taps | 5 | 5 |
| Radio again after a choice | 5 replays | 5 |
| Read during speech, then mode switch | current state only | matches; no stale line |

Runtime `allLines()` exactly matches the 59-line manifest. Read map reads its instruction; Read with Sound off still speaks. No stale Crew welcome follows a job or Mission entry.
Initial CDP batches disconnected, including a smaller retry. The original control and later targeted batches recovered; failed runs are not counted as passing evidence.

#### Facts checked

Named sources checked live on 2026-11-05; calculations are in `review-numbers.json`.

- Two-week daylight/night: [NASA LADEE press kit](https://science.nasa.gov/wp-content/uploads/2023/05/ladee-press-kit-08292013.pdf). 29.5 / 2 = 14.75 Earth days; notes name polar exceptions.
- One-sixth weight: [NASA Moon Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html), 1.62 / 9.80 = 0.1653; spec's 9.81 gives 0.1651. Mass does not change.
- Cold nights: [NASA Weather on the Moon](https://science.nasa.gov/moon/weather-on-the-moon/), about minus 133 C near the equator; [USDA FSIS](https://ask.fsis.usda.gov/article/What-is-the-right-temperature-for-the-freezer), home freezer about minus 18 C. Universal claim corrected. Spec conversion is also wrong: minus 130 C is minus 202 F, not minus 208 F.
- No breathable air or liquid rivers: [NASA Moon Facts](https://science.nasa.gov/moon/facts/), unbreathable exosphere and no liquid surface water. The air-loss scene assumes a pressurized base.
- Dark polar crater ice: [NASA/JPL, Ice Confirmed at the Moon's Poles, 2018](https://www.jpl.nasa.gov/news/ice-confirmed-at-the-moons-poles/). Notes distinguish observed patchy ice from the drama's convenient large block and retrieval.
- Sharp, clinging dust and suit brushing: [NASA lunar regolith hazards](https://science.nasa.gov/biological-physical/what-hazards-are-caused-by-lunar-regolith/) and [Gaier, NASA/TM-2005-213610](https://www.nasa.gov/wp-content/uploads/static/history/alsj/TM-2005-213610.pdf). Brushing removes some dust, not all.
- PV sunlight and batteries: [US DOE solar basics](https://www.energy.gov/cmei/systems/how-does-solar-energy-work) and [solar/storage basics](https://www.energy.gov/cmei/systems/solar-integration-solar-energy-and-storage-basics). Dots do not claim actual two-week battery capacity.
- Plant light, water, air and suitable temperature: [ESA AstroFarmer PR42](https://climatedetectives.esa.int/wp-content/uploads/2023/09/PR42_AstroFarmer-1.pdf). Nutrients and a sealed heated base are assumed.
- Blankets conserve existing warmth: [US DOE Consumer Guide to Home Insulation](https://www.energy.gov/sites/default/files/2021-11/ES-HomeInsulation_081721E-a.pdf). Notes say insulation is not a heat source.
- Cr3 revision, Re9 discussion and Cn11 subject connections: [NCAS Theatre at a Glance](https://nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf). Children reperform a choice, discuss its effect, and use Moon science in role. NGSS is context only.
- Heathcote and Bolton, *Drama for Learning*, Heinemann, 1995: authors/date checked against [WorldCat](https://search.worldcat.org/title/30624219); full book not read.

#### Sensitivity

None: fictional Moon crew and science, no cultural, religious, Indigenous, hard-history or body instruction. Empty suits are equipment; the real class supplies the people. No painted person needs a people flag.

#### Flattest moment left

Brush off remains a static airlock while the class mimes dust removal. The crew's performance carries it. The formerly flat water answer now has a loaded-rover payoff.

#### Graphics

All 14 final assets inspected: six prop cutouts, five settings, rover, ice and planter. One crater replacement plus one targeted revision; other strong paintings kept.
Built-in image tool, final `art/raw/ice-crater.png`, required free `art.py --rekey ice-crater`, final `art/ice-crater.webp`; full prompt in `art/prompts.json`, original retained in Scratch.
No missing art tokens/files. Bundle 1,509,808 bytes; art 1,080,402 bytes. Nothing removed for size. Compared with existing Snowy Mail Route and Beat Lab bar frames.
Contrast: white/brand 9.08, brand/paper 8.17, ink/paper 14.92, muted/paper 6.00, ink/Ada 15.63, all AA for text shown.
Inspected cold play, all seven desktop/preview sizes, changed scenes at 680/1366/760, all eight initial endings, modal and voice frames. Phone Crew, battery, water, night and map checked at a real 375 px iframe; the two phone repairs re-shot. Real keyboard-only R, Escape and A shortcuts also passed.

#### Audit

Ran once, last, with a 2,400-second limit: completed, exit 0, 18 leads. Full result: `_scratch/moon-base-drama/review-audit/audit.md`.

- Two iframe leads: the audit could not attach to the child context, so it also reported no hint. Direct 375 px host checks passed, including Read and the longest message. This follow-up found the final phone spacing collision; repaired and re-shot Crew, night and first beat.
- Seven welcome leads: six badge taps and a guarded Mission tap speak their own fitting line. Skipping the unmarked welcome follows the spec and first-tap rules; no late welcome follows them.
- Nine quick-tap leads: Crew/Motion welcomes, the guarded-entry how and six first-job transmissions are cut by the next tap. This is the explicit interrupt-on-any-tap rule; how-to lines are marked when they start. Read can repeat the current instruction.
- All five-click repeat checks clean; no console errors, undersized targets, desktop clipping/overlap, focus failures, infinite calm animation, resize exceptions or stuck controls. All 64 audit PNGs inspected through six labelled sheets.
The job gate means the automatic mode walk stays on Crew. Separate eight-path, main-voice, replay and keyboard runs cover Mission. The phone-only spacing fix followed the audit; affected 375 px states were rechecked. No second audit was run. Both bundle hashes are preserved in `review-validation.json`.

#### Left open

No audio recorded: browser speech works; firm-captain/Alnilam timbre and classroom audibility await the separate recording workflow.
The shared kit remembers Motion on this device. Story/jobs are not saved or sent. Kit persistence opt-out and recorded-playback glow callbacks remain in handoff; shared source files unchanged.
Unattended decisions followed spec/baseline without questions. No mode, topic, score or kit feature added. Science corrections and ordinary choice-order/commit behavior support the existing lesson.
Process note: the first two read-only bootstrap commands were not timeout-wrapped; they completed immediately. All later commands used the bounded runner. Review browsers/servers are closed; temporary host.html removed.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 1 (general 1, family 0), should fix 5 (general 5, family 0), polish accepted 7

### Refine: moon-base-drama

Merged from refine/teaching.md, refine/play.md and refine/craft.md. No sensitivity review needed (no cultural, Native
or hard-history content; all three lenses agree). Not a Curiosity. Integrator spot-checks: src.html:390-412 (choice
glyphs), :585-595 and :640-665 (rewind buttons and map), :709-725 (goBeat), :847-853 (radioState).

#### Blocker
1. **A rewind past skipped choices plays a story the map contradicts.** src.html:651 (`button.disabled = n >
   state.visited`) with :709-725 (`goBeat`: `invalidateFrom(beat)` moves later choices to `oldChoices`, but
   `state.visited` stays at its maximum). After a full run, Rewind to Batteries, then Rewind to Warmth jumps straight to
   beat 6 with no Batteries or Water choice made. The map still shows the sun-battery and ice icons on those nodes, not
   faded (they are before the current beat), while the meter reads Light 1, Water 1; choosing the blanket ends on "the
   plants are droopy" under a map showing three good choices. Integrator check: the same happens through Back (Back
   from beat 8 to beat 3 also invalidates later choices and leaves `visited` at 8). Seen in teaching
   out/rw-d-jump6-end.png (meter 1,1,3, endLow) and the rw-b/rw-c drive shots. Fixed looks like: whenever choices are
   invalidated (rewind or Back), `state.visited` drops to that beat, so a map button is enabled only for a choice beat
   already reached on the current path; a node with no current choice shows its number or faded old icon, never a
   live-looking old choice before the current beat. This also covers the play nit that Rewind offers Batteries on beat
   3 before any battery choice exists (audit state-rewind-open-1366x768.png): enable a node only once it is behind the
   current beat or has a current choice. Re-run Done when 3 with two rewinds in a row and with Back then Rewind. (general)

#### Should fix
1. **A child alone never hears the question or the two choices.** Choice beats 3, 4, 6; src.html:335-336 (choice
   buttons), :469 (`read`). BASELINE rule 4 (defaults work for a solo user) and STANDARDS K-2 ("a narrator voices every
   fixed line"): the question is only on Ada's card (never spoken, by design) and the choice words are never spoken, so
   a pre-reader hears a fact, then "Commander, read your card...", then faces two buttons it cannot read. Seen: audit
   state-batteries-1366x768.png; teaching log v-slow; play finding 3. Fixed looks like: Mission Control voices the two
   crew lines on each choice beat, after the beat's fact line, as the crew's options ("Crew, you could say: Fill the
   batteries now! Or: Wait until dark."), in the shuffled order shown on screen, and Read on an open choice beat speaks
   the beat line plus the options. Ada's card stays unspoken (Done when 4 still holds). New lines go in voice/lines.json
   and `allLines()`. (general)
2. **The night ending barely changes, so "watch the story change" does not land.** Beat 8; src.html:113-115, :657-663.
   The painted greenhouse behind is lush and lit on every ending; the only change is the lamp beam count and a
   `scaleY(.55)` on one foreground planter, which reads as shorter, not wilted, and the two-full and none-full endings
   look the same. "The plants are droopy" plays over a thriving greenhouse. Seen: play/shots/b8-allB.png (1,2,1),
   b8-two.png (3,2,3), audit state-night-1366x768.png (3,3,3), teaching out/rw-d-jump6-end.png. Fixed looks like: each
   meter gap has its own picture, drawn in code: leaves that clearly hang and yellow (not a vertical squash) when Water
   is low, a frost or blue chill tint when Warm is low, the whole scene (background too) darker and desaturated in
   proportion to Light, so a class comparing two runs can point at what changed. Motion off: the end state at once.
   (general)
3. **Choice icons are text glyphs a pre-reader cannot read; the door is an empty box.** src.html:397 "☀ ▣", :399 "☾",
   :403 "≈", :409 "▧", :410 "▯" (only :402 🧊 is a real picture). Seen: play b6-warmA.png, b6-warmB.png,
   b8-map-open.png; craft out/warm-680.png, out/zoom-map-375.png (the two-glyph "☀ ▣" spills out of its 20 px map
   diamond and "▯" renders as an emoji box). Fixed looks like: small drawn SVG icons (battery with a sun, moon, ice
   cube, wave, folded blanket, door), one icon each, the same on the choice button, the map node (fits the diamond) and
   the Rewind dialog; `.choice-icon` and the map dots get `aria-hidden="true"` so screen readers read the words, and
   `#map-strip` gets a role to match its aria-label (craft nit 7). (general)
4. **The premise is lost when the first tap is a job badge, and never comes back.** src.html:467 (welcome valid only
   while no job is checked). The screen invites a badge tap first; then "Teacher, you are Commander Ada" is never
   heard: Sound off and on and Crew re-entry bring nothing, so standard voice check item 3 fails. Mission first gives
   "Tap a job badge" and the welcome is never heard either. Seen: craft log v-job-first-then-sound, play vlog-mf.json,
   audit rows 1 and 5-10. Fixed looks like: a welcome form that stays true once jobs exist (the premise without "Tap a
   job badge"), brought once by Sound on or the next Crew entry, or carried once at Start mission. (general)
5. **The radio glow follows speech synthesis, not Mission Control.** src.html:847-853 (`radioState` uses
   `speechSynthesis.speaking`). `Curio.init({clips:"voice:*"})` plays recorded clips through `Audio` first, so once
   this tool's clips land the radio will never glow while Mission Control talks, and a Read line will not show in the
   caption (spec: "The radio glows only while Mission Control speaks"). Seen: code against kit/curio.js speakOne.
   Fixed looks like: glow and Read caption follow `V.playing` or an active Read, whatever the audio path. (general)

#### Polish accepted
1. **Endings: the story line first, then the how-to.** src.html:458 (`guide('reflect', ...)`). The full-success
   ending opens with "Tell Ada which choice helped. Tap Rewind." before "Great work, crew!", and tells a crew that just
   won to rewind. On the three ending lines only, speak the ending line first and the reflect how-to after it, and word
   it for both ways on ("Tap New mission, or Rewind to try another way."). Seen: audit state-night-1366x768.png caption,
   play vlog-full.json, teaching v-five. (general)
2. **Warmth choice A has no referent.** src.html:409: "Wrap it in a blanket" becomes "Wrap the greenhouse in a
   blanket" (button, map, rewind card, lines.json). Seen: play b6-warmA.png. (general)
3. **Ada's card reacts to each result.** src.html:623-624. After a choice the card keeps the question just answered;
   only beat 3 B has a response. Add one short in-role reaction per result on the card (for example "Great work, Rover
   Driver! Bring it home."; for a B result, a nudge toward Rewind like the existing one). Card only, never spoken. Seen:
   play b3-choiceA.png, b4-choiceA.png, b6-warmB.png. (general)
4. **Rewind invites the crew to say the new line their own way.** On a rewound choice beat, Ada's card adds "Say the
   new line in your own words. What will you tell me?" This gives grade 2 TH:Cr3 (adapt dialogue) a real ask. Card only.
   (general)
5. **Teacher notes name what TH:Re9 actually asks.** notes.md "Good to know": name the real asks: choose a prop for
   your job, say how the crew met each moon problem, which choice mattered most and why; Talk about it may add "How did
   the crew act when the doors opened?" (general)
6. **"Back to base" in the Rewind dialog becomes "Back to the story".** src.html:363; "base" is also the Crew screen.
   Seen: play b8-map-open.png. (general)
7. **Crew at 1920x1080: label and subtitle crowding.** The scaled watering can (scale 1.12) touches the "Plant Keeper"
   label and the subtitle "Choose a job. Mime your prop." sits on the first badge's top border. Give both a little
   room; props may also grow inside the large badges. Seen: craft out/zoom-crew-1920.png. (general)

#### Settled calls
- Solo child versus teacher in role (teaching 2 "may be a spec question", play 3 should fix): BASELINE rule 4 wins, so
  it is a should fix, and the fix stays inside the spec: voice the crew's two options, never Ada's card. A fuller solo
  path goes to the spec's open questions below.
- Ending picture (teaching polish, play should fix): should fix. It is the Re9 payoff and the picture contradicts the
  spoken ending.
- How-to inside the transmission ahead of the story (play polish 4, teaching nit 7): keep the order on beats 2 to 7.
  It is deliberate (src.html:440-441: a fast Next cannot strand a how-to behind a cut line) and the voice check passes.
  Only the endings change (polish 1), where no fast Next follows.
- Two quick taps cutting a line (audit rows): correct, not a fault. Done when 5 says any tap stops the radio at once;
  job lines are events that replay on the next tap.
- Ada's card toggle and Motion stopping the radio (craft nit 8): to spec ("any tap stops the radio"); Radio again
  recovers the line. Do not change.
- Facts and the 8 meter paths: all three lenses passed them; the on-screen wording ("colder than a home freezer", "no
  air to breathe outside") is a little softer than the spec and still true. Do not change.

#### To the spec's open questions
- Should a solo child have a path that does not start with "Teacher, you are Commander Ada" (for example the child plays
  Ada, with the card read aloud in that mode)? Today the spec makes the teacher the commander and never speaks the card.
- Warmth choice B "Open the doors for air" answers a different question than "How do we keep the plants warm?", so it
  reads as a joke more than a misconception (teaching 5, play 5). A warmth idea the radio's facts refute (for example
  "Open the windows to let the Sun in") would teach better, but it changes the spec's content and result line.

#### Not taken
- Job badge cannot be unchecked (play nit 9): a repeat tap replaying the job line is useful in class; not worth the change.
- Hint text 11 px at 375 wide (craft nit 6): the radio caption carries the same words at a readable size.
- Droop following Light (teaching 6): the spec ties Light to the lamps; should fix 2 darkens the scene by Light instead.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: moon-base-drama (round 1)

Cold lens on the bundle as built (`moon-base-drama.html`, 1,509,808 bytes). Not re-bundled. Frames and logs in
`S:/CurioClass-codex-scratch/moon-base-drama/craft/out/` (mine) and `S:/CurioClass-codex-scratch/moon-base-drama/audit-r1/` (shared audit).

#### Contract (clean)

- One file, 1.51 MB: under the 2 MB goal.
- No network requests: `performance.getEntriesByType('resource')` empty after a full walk to the ending (perf-night).
- No console errors or exceptions in any of my 20 shots or in the audit.
- Kit used: `Curio.voice`, `Curio.init`, kit Motion, Sound, Read and `.calm`; nothing re-implemented except the radio caption and glow loop (finding 1).
- Frame times at 1366x768 (rAF, 180 to 240 frames): Crew idle median 16.7 ms, p95 16.7; rover drive 16.7 / 16.7;
  night scene 16.7 / 16.8. Only the idle beacon and the drive or ice float run, all killed by Motion off (calm-rover, calm-ice: zero animations, rover transform none).
- Keyboard: Tab reaches the badges with a 4 px #ffcf45 outline (kbd-tab); Right and Left step beats, Right stops on an unanswered choice, A toggles the card, R opens the map with focus on its first choice (kbd-letters).
- Targets: the audit's 60 px rows are clean at every size; I cite them.
- Art: all 14 `art:` tokens have prompts.json entries; no people in any asset (airlock suits hang empty, checked on the frame). Credit line matches CODEX-BUILD.
- Words: no em dashes in src.html or notes.md; "Curio Class" only; privacy stated in notes (story in memory, Motion preference on this device).
- Lines: voice/lines.json holds all 59 strings, including the 24 guided "how + event" joins, word for word with `allLines()`.

#### Findings

1. **should fix, general.** `src.html:847-853` (radioState). The radio glow and the Read caption follow
   `speechSynthesis.speaking` only. The tool ships no clips yet (voice/ has only lines.json), but sibling tools ship
   mp3 clips and `Curio.init({clips:"voice:*"})` plays them through `Audio`, not speechSynthesis. Once this tool's
   recordings land, the radio will never glow while Mission Control talks, and a Read line will not show in the caption
   (spec: "The radio glows only while Mission Control speaks"). How seen: the code against `kit/curio.js` speakOne
   (clips first, then speechSynthesis). Better: glow on `V.playing` or an active Read, not on the synth.

2. **should fix, general.** `src.html:467` (welcome valid only while no job is checked). A first tap on a job badge
   skips the welcome (kit rule, fine), but it never comes back: Sound off then on, and Crew re-entry, bring nothing
   (log v-job-first-then-sound: only the job line, then the beat 1 line). Standard voice check item 3 fails, and the
   most natural first tap means the teacher never hears "Teacher, you are Commander Ada." Better: a welcome that stays
   true once jobs exist (the premise without "Tap a job badge"), brought by Sound on or the next Crew entry, once.

3. **should fix, general.** Choice icons are bare text glyphs: `src.html:397` "☀ ▣" (sun and battery), `:409` "▧"
   (blanket), `:410` "▯" (door), `:403` "≈" (river), beside one real emoji `:402` 🧊. In a K-2 tool the icon is
   what a pre-reader sees on the big choice button; a hatched square and a tall rectangle do not read as a blanket or
   a door. Frames: out/warm-680.png, audit state-batteries-1366x768.png. Better: small drawn SVG icons (battery
   with a sun, blanket, door, wave), the same on the choice, the map node and the rewind card.

4. **polish, general.** Map strip choice nodes: the two-glyph "☀ ▣" spills out of its 20 px diamond, and "▯" renders
   as a colored emoji box (out/zoom-map-375.png; also visible at 680x425, audit state-night-680x425.png). Better: one
   icon per node that fits the diamond (follows from finding 3).

5. **nit, general.** Crew at 1920x1080 with a badge checked: the scaled watering can (scale 1.12) touches the
   "Plant Keeper" label, and the subtitle "Choose a job. Mime your prop." sits on the first badge's top border
   (out/zoom-crew-1920.png). Props are also small in the big badges (max-height 135 px in about 330 px badges).

6. **nit, general.** Hint text is 11 px at 375 wide and in short windows, 14 px at 1920x1080 (crew-375-hint; audit
   frames). The radio caption carries the same words, so nothing is lost, but the bar hint is hard to read on a projector.

7. **nit, general.** Screen readers read the choice glyphs ("☀ ▣") before the words: `.choice-icon` (`src.html:335-336`)
   and the map dots have no `aria-hidden`; `#map-strip` has an aria-label but no role.

8. **nit, general.** `src.html:804-809` and `:841-845`: Ada's card toggle and Motion call `stop()`, so
   hiding the card mid-transmission cuts the beat's fact line. The spec says any tap stops the radio, so this is to
   spec; Radio again recovers it. Consider letting the card and Motion leave the radio playing.

#### Standard voice check

Held clicks (0.12 s), Sound and Motion on, 1366x768. Logs: run on shots1.json and shots2.json in my scratch folder.

| line | kind | expected | spoken |
|---|---|---|---|
| "When the crew is ready, tap Start mission." (joined to the first job line) | how | 1 in 5 badge taps | 1 |
| Plant Keeper job line | event | 5 | 5 |
| "When the crew is done, tap Next." (joined to beat 2) | how | 1 | 1 |
| "Commander, read your card. When the crew answers, tap their choice." (joined to beat 3) | how | 1 | 1 (beats 4 and 6 plain) |
| batteries result B, choice tapped three times | event | 3 | 3 |
| "Tell Ada which choice helped. Tap Rewind." (joined to the ending) | how | 1 | 1 |
| ending line, Radio again three times | event | 3 | 3 |
| beat lines 1 to 7 | event | each beat opened | every one |

1. Repeats: pass (table). Audit five-clicks rows clean.
2. Stale lines: pass. Nine taps 0.2 s apart ending on Crew: every line cut by `hush`, nothing spoken after the Crew
   tap (v-fast). Back from beat 4 speaks beat 3's line, not the dropped result.
3. First-tap timing: stage tap gives the welcome at once (v-first-stage2); ArrowRight gives the welcome (v-first-key);
   Read speaks the hint only (v-first-read); Sound says nothing, Sound on brings the welcome once (v-first-sound);
   a badge gives only its own line. **Fail on the skipped welcome returning (finding 2).**
4. Read: cuts the playing line and speaks the beat line; with Sound off it still speaks (v-read-soundoff); the next
   tap after Read starts its line at once (v-read-mid).
5. Order: spoken lines follow the taps in every log.

#### Audit pilot

- Leads confirmed: "welcome not heard" after a first tap on a job badge, and my run shows it never returns (finding 2).
- Leads wrong (as defects): "two quick taps, line cut and never heard whole" on the badges and mode buttons. The spec
  says any tap stops the radio at once, and job lines are events that replay on the next tap. "Not heard" after a
  first Mission tap with no crew: it speaks "Tap a job badge" instead, which names the action, and Sound on still brings the welcome.
- Missed: the glyph icons (3, 4), the radio glow tied to speech synthesis (1), the welcome never coming back (2),
  the 1920 badge crowding (5).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: moon-base-drama (round 1)

Played twice: as a K-2 child alone at home, and as a teacher projecting it as Commander Ada. Bundle as built, not re-bundled.
Frames: shared audit `S:/CurioClass-codex-scratch/moon-base-drama/audit-r1/` (all sizes, every state) plus my own in
`S:/CurioClass-codex-scratch/moon-base-drama/play/shots/` (every beat at 1366x768, all three endings, rewind from the end,
map at the end, Motion off on beat 4, 680x425 beats 1, 5 and 8) and voice logs `play/vlog-full.json` (full run plus a
rewind, held clicks 2.5 s apart), `play/vlog-fast.json` (0.3 s taps, Back, mode switch), `play/vlog-mf.json` (Mission first).
No console errors in any run. Nothing cultural, Native or hard-history: no sensitivity review needed.

#### Findings

1. **The ending barely changes, so "watch the story change" doesn't land.** Where: beat 8, src.html:113-115, 657-663.
   What: the payoff of the whole tool is the night greenhouse, but the three endings look nearly the same. The painted
   background (lush tomatoes, healthy beds) is identical for every ending, so "the plants are droopy" plays over a
   thriving greenhouse. The only changes are the number of lamp beams and a `scaleY(.55)` squash on one small planter,
   which reads as shorter plants, not wilted ones; the two-full and none-full endings use the same squash. A K-2 class
   comparing two runs after a rewind sees almost nothing. Better: wilt that is unmistakable (leaves hanging, yellowed,
   tomatoes dropped), apply it to the whole greenhouse (or a darkened, desaturated background when Water or Warm is low),
   and a frost or chill cue when Warm is low, so each meter gap has its own picture. How seen: `play/shots/b8-allB.png`
   (1,2,1), `b8-two.png` (3,2,3), audit `state-night-1366x768.png` (3,3,3). Level: **should fix**. Tag: general.

2. **Choice icons are abstract glyphs a pre-reader can't use; one shows as an empty box.** Where: src.html:397-410.
   What: the spec asks for icons (sun and battery, moon, ice cube, wave, blanket, door) because K-2 children can't read
   the button words. The build uses text glyphs: "☀ ▣" for batteries, "≈" for a river, "▧" for a blanket, and "▯" for
   the door, which renders as a plain empty rectangle that looks like a missing character. Only the ice cube is a real
   picture. The same glyphs appear on the map strip and in the Rewind dialog. Better: drawn SVG or painted icons
   (battery with a sun, wave, folded blanket, door). How seen: `b6-warmA.png`, `b6-warmB.png`, `b8-map-open.png`,
   `b3-choiceA.png`. Level: **should fix**. Tag: general.

3. **A child alone can't hear the question or the choices.** Where: src.html:469 (Read), 335-336 (choice buttons).
   What: rule 4 says defaults must work for a solo user. Alone, a K-2 child hears Mission Control's line, but Ada's
   question is never spoken (by design) and the two choice buttons are words only, so a pre-reader on a choice beat
   hears "Commander, read your card. When the crew answers, tap their choice." and then has nothing they can read. Read
   repeats Mission Control, not the options. The welcome also tells a lone child "Teacher, you are Commander Ada".
   Better, without breaking the teacher-in-role design: speak the two crew lines as part of the choice beat ("Crew, you
   could say: Fill the batteries now! Or: Wait until dark."), or let Read on a choice beat say the two options. How
   seen: `state-batteries-1366x768.png` and the code path above. Level: **should fix** (the integrator may weigh this
   against the K-2 teacher-led band in STANDARDS.md). Tag: general.

4. **The how-to goes ahead of the story in Mission Control's voice and on the radio caption.** Where: src.html:440-458
   (`guide`), caption at 518-519. What: the first time each step comes up, Mission Control opens with a UI instruction
   ("When the crew is done, tap Next. The ice block is heavy...") and the radio caption keeps that text on screen. It
   breaks the radio fiction for the class, and it buries the moment: the best beat in the tool, the full-greenhouse win,
   opens with "Tell Ada which choice helped. Tap Rewind." before "Great work, crew!", and tells a crew that just won to
   tap Rewind. Better: story line first, instruction after it (or in the hint only, with the voice at the end), and on
   the all-full ending say "Tap New mission, or Rewind to try another way". How seen: `state-night-1366x768.png`,
   `b5-lift.png`, `b2-greenhouse.png`, `vlog-full.json` (reflect_endTwo). Level: **polish**. Tag: general.

5. **Two choice lines don't make sense as answers.** Where: src.html:409-410, beat 6. What: Ada asks "How do we keep the
   plants warm?" and the crew line is "Wrap it in a blanket" ("it" has no referent; the scene is an airlock with space
   suits). The other option, "Open the doors for air", is not an answer about warmth at all, so a child can't reason to
   it as a tempting mistake. Better: "Wrap the greenhouse in a blanket" against a warmth answer that is wrong for a moon
   fact, for example "Open the windows to let the Sun in" (no Sun at night, and the air would rush out). How seen:
   `b6-warmA.png`, `b6-warmB.png`. Level: **polish**. Tag: general.

6. **Ada's card has nothing to say after a choice.** Where: src.html:623-624. What: after a choice the card keeps the
   question that was just answered; only beat 3, choice B, gets a response ("Hmm. Should we rewind and try again?").
   The teacher in role has no line for the good outcomes or for the river and open-doors results. Better: one short
   reaction line per result on the card ("Great work, Rover Driver! Bring it home."). How seen: `b3-choiceA.png`,
   `b4-choiceA.png`, `b6-warmB.png`. Level: **polish**. Tag: general.

7. **The premise is lost if the first tap is a badge or Mission.** Where: src.html:467. What: the welcome ("Teacher, you
   are Commander Ada. Tap a job badge for each crew member.") is dropped when a badge is tapped first, which is what
   the screen invites ("Choose a job. Mime your prop."), and it never comes back. Mission first gives "Tap a job badge"
   and then the badge line; the welcome is never heard. Better: bring the premise back once in the first job line or at
   Start mission. How seen: audit table rows 1 and 5-10, confirmed in `vlog-mf.json`. Level: **polish**. Tag: general.

8. **"Back to base" in the Rewind dialog.** Where: src.html:363. What: it closes the dialog and returns to the story,
   but "base" is also the Crew screen's name (Moon Base Luna), so a teacher may expect to go to Crew. Better: "Back to
   the story". How seen: `b8-map-open.png`. Level: **nit**. Tag: general.

9. **A job badge can't be unchecked.** Where: src.html:559-566. What: badges look like toggles (aria-pressed, a check),
   but a second tap only repeats the line; a mistaken tap stays checked. Level: **nit**. Tag: general.

10. **Rewind offers Batteries before any battery choice exists.** Where: src.html:651. What: on beat 3 with no choice
    yet, Rewind enables Batteries, which "rewinds" to the beat already showing and says "Rewinding to the batteries".
    Better: enable a node once its choice is made. How seen: audit `state-rewind-open-1366x768.png`. Level: **nit**.
    Tag: general.

What works: the beats read well aloud at a teacher's pace, every tap cuts the radio at once and nothing stale followed
in the fast run, Back undoes a choice, rewinding from the end restores the meter and fades later nodes (`b8-rewind-water.png`:
3,1,1 with Warmth faded), all three endings are reachable and correct, the choice order varies, and the painted scenes
are inviting at every size including 680x425 and the 375 iframe.

#### Audit pilot

- Confirmed: the welcome is not heard after a first tap on a badge or on Mission (finding 7; `vlog-mf.json`).
- Wrong or by design: "two quick taps cut the line" rows. The spec wants any tap to stop the radio at once (Done when 5),
  so a line cut by the second tap is correct here, not a fault. All size and state rows were clean and held on my frames.
- Missed: glyph icons and the empty-box door (2), the near-identical endings (1), choices unreadable for a lone
  pre-reader (3), how-to before the story in the voice and caption (4), and the choice wording (5, 6). None of these are
  mechanical.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: moon-base-drama (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json, audit-states.json and the shared audit
(S:/CurioClass-codex-scratch/moon-base-drama/audit-r1). My own frames and logs are in
S:/CurioClass-codex-scratch/moon-base-drama/teaching/out (driven with scripts/drive.py, held clicks, port 9887).
Standard text was checked against the NCAS theatre performance standards (New York's adopted set, K, 1 and 2).

#### Findings

##### 1. Rewinding twice skips choices, and the meter then contradicts the story map (blocker, general)
- Where: src.html:585-595 (rewind buttons), :651 (`button.disabled = n > state.visited`), :709-725 (`goBeat` with
  `rewound`).
- What: after a full run, Rewind to Batteries moves every choice to `oldChoices`, but `state.visited` stays at 8, so
  Water and Warmth stay enabled in the map. Rewind again to Warmth jumps straight to beat 6 with no Batteries or Water
  choice made. The story map still shows the sun-battery and ice icons on those nodes, not faded (they are before the
  current beat), so the class sees "we chose batteries and ice", while the meter reads Light 1, Water 1. Choosing the
  blanket and going on gives "The long night is here, and the plants are droopy" on a path whose map shows all three
  good choices. The tool tells K-2 children their right science choices failed. A meter that misleads is a blocker
  (REFINE, Rounds). Done when 3 also fails: the rewind does not restore a consistent story.
- How seen: drive shots rw-b-skip (after Rewind to Batteries: `dis:[false,false,false]`, old `{3:0,4:0,6:0}`),
  rw-c-jump6 (beat 6, meter 1,1,1, Batteries and Water nodes carry old icons, not `future`), rw-d-jump6-end
  (meter 1,1,3, `endLow`), frame out/rw-d-jump6-end.png.
- Better: a rewind sets `visited` back to the rewound beat (only reached choices can be rewound to), or the skipped
  nodes show as faded old story and the map buttons after the current choice stay disabled until reached again.

##### 2. A child alone never hears the question the science choice answers (should fix, general; may be a spec question)
- Where: spec "Ada's card, not spoken", Done when 4; src.html:396, :401, :408 (`ada:` lines), the welcome
  "Teacher, you are Commander Ada."
- What: the choice questions ("How do we keep the plant lamps on all night?", "Where can we get water?", "How do we
  keep the plants warm?") live only on Ada's card, which is never spoken, and the choice labels are not spoken
  either. With a teacher this is the design and it works. A pre-reader alone at home (BASELINE rule 4) hears a fact
  and then sees two buttons with no question, so TH:Cn11 (apply the moon fact to a choice) does not happen. The K-2
  teacher-led guardrail softens this, so the merge may route it to the spec's open questions. A small fix inside the
  spec: Read on a choice beat could speak the choice labels ("Fill the batteries now, or wait until dark?") as
  Mission Control asking the crew, keeping Ada's card unspoken.
- How seen: src.html read; voice log v-slow shows only Mission Control lines at beats 3 and 4.

##### 3. TH:Cr3 at grade 2 is thin: the crew never adapts dialogue (polish, general)
- Where: the choice beats (spec "Mission", notes "Say the crew's line before tapping its choice").
- What: NCAS TH:Cr3.1.2a is "Contribute to the adaptation of dialogue"; grade 1 is adaptation of the plot. Rewind
  teaches plot revision well (K: answering Ada's questions also covers Cr3.1.K a). For grade 2 the crew only picks
  between two fixed lines. Better: on a rewind, Ada's card adds "Say it your own way" (for example "Rewinding to the
  batteries" card: "Say the new line in your own words. What will you tell me?"), so the class rewrites the line, not
  only switches buttons. Cheap and inside the spec.
- How seen: standard text vs. src.html:395-410.

##### 4. TH:Re9 is described by its effect, not by what the code asks (polish, general)
- Where: spec "Who and how", notes "Good to know" ("TH:Re9 (explain its effect)").
- What: TH:Re9 K-2 is evaluate dramatic play, select or use props, and discuss or describe how characters respond to
  challenges. The tool does all three (job props, the ending question, the crew meeting each moon problem), but the
  notes don't say so, so a teacher can't see the match. Better: notes name the real asks: "choose a prop for your
  job (Re9 b), say how the crew met each moon problem and which choice mattered most (Re9 a, c)". Talk about it
  could add "How did the crew act when the doors opened?" for Re9 c.
- How seen: NCAS text vs. notes.md.

##### 5. The Warmth wrong choice doesn't answer the warmth question (polish, general)
- Where: src.html:407-410, beat 6.
- What: Ada asks "How do we keep the plants warm?" and option B is "Open the doors for air", which answers a
  different question, so it reads as a joke rather than a misconception the fact corrects. Option A, "Wrap it in a
  blanket", has no antecedent for "it" (Ada said "the plants"). Better: A "Wrap the greenhouse in a blanket"; B a
  warmth idea the two facts on that radio line refute, for example "Open the doors to let warm air in" (result:
  outside is colder than a freezer and has no air).
- How seen: src.html; frames state-water-result, my v-five log.

##### 6. The ending picture barely shows what the meter says (polish, general)
- Where: src.html:113-115, :657-663 (night, lamps, leaf droop).
- What: Re9 hinges on "which choice made the biggest difference", but the full and droopy endings look nearly the
  same: the painted greenhouse plants behind stay lush and lit, and only the small foreground tray is squashed
  (scaleY .55), which reads as shorter, not wilted. Light 1 still shows a big lit lamp, and droop ignores Light, so
  "no batteries" ends with upright plants. Better: droop and dim also follow Light, and the background plants darken
  more when a meter is low, so children can point at what changed.
- How seen: audit frame state-night-1366x768.png (all full) beside my out/rw-d-jump6-end.png (1,1,3, droopy); path
  walk `100 ... lamps=1 droopy=false`.

##### 7. The full-success ending opens with an instruction (nit, general)
- Where: src.html:458, guided `reflect_endFull`.
- What: the first ending heard says "Tell Ada which choice helped. Tap Rewind." before "Great work, crew!", so the
  payoff lands after a how-to. Put the how-to after the ending line, or let the hint carry it.
- How seen: audit frame state-night-1366x768.png caption; voice log v-five last line.

#### Checks that passed
- Done when 2: all 8 paths (path walk in the tool, `paths` shot): meter 1,1,1 at beat 2; A gives +2, B gives 0, 1, 0;
  AAA ends full, any single B ends two full, two or three B end low. Every ending is reachable and matches the meter.
  Recomputed by hand: matches the spec's check.
- Done when 3 (single rewind): Rewind to Water from the end restores Light 3, Water 1, Warm 1 and fades later nodes
  (rw-e). Fails only in the double-rewind case above.
- Done when 4, 5, 7: voice logs v-slow, v-fast, v-five: no Ada line is ever spoken; each Mission Control line plays
  when its beat opens; Radio again replays the result; fast taps cut lines with no stale line after; how-to lines once.
- Done when 1, 6, 8, 9: audit rows clean at every size and state; Next is disabled on an open choice beat and the
  choose line does not name it (state-batteries-680x425.png).
- Facts, spot-checked against a second source: lunar night near the equator -208 F (-133 C) (NASA Weather on the
  Moon), so "colder than a home freezer" holds; gravity one sixth (NASA Moon Facts); exosphere, not breathable air
  (NASA Moon Facts); ice in permanently shadowed polar regions (NASA Moon Facts); 29.5 / 2 = 14.75 days ("about two
  weeks"); 1.62 / 9.81 = 0.165 ("about one sixth"). Water B line ("found ice late, tank still low") matches Water +1.
- Notes: What it teaches, Key skills and Support at home are true of this tool, and the home ideas are doable tonight.
  No sensitive topics, no hard history, nothing cultural or Native: no sensitivity review needed.
- Guardrails: teacher-led K-2, no score; the check on a job badge is stated as not a score.

#### Audit pilot
- Leads confirmed: none of its 16 voice leads bear on teaching (the "welcome not heard" after a first badge tap is by
  design: the badge line carries the premise; Craft owns it).
- Leads wrong: none checked.
- What it missed: the double-rewind skip (finding 1). Its rewind-open state opens the map once from beat 3 and never
  rewinds twice, so a contradiction between map and meter could not show. The weak ending contrast (finding 6) is a
  "what one look means" item it can't judge.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: moon-base-drama (Codex fix, round 1)

Evidence paths are relative to `_scratch/moon-base-drama/`. Claimed frames were inspected. The reported rewind bug is repaired, but the prescribed option wording still permits a longest-text shortcut. Under the user's stronger no-skill-pass rule, the meter blocker is conservatively NOT FIXED. No questions were asked in this unattended session; scope decisions preserve the spec and settled calls.

#### Blocker

1. **NOT FIXED under the additional no-skill-pass condition; the reported rewind corruption is repaired.** Before: `fix-before/double-rewind.png`, `back-rewind.png`, `skip-to-warmth.png` and their `before-*.json` files show visited 8 at beat 3, every target enabled, and an invalid 1,1,3 ending under three live-looking old icons. Invalidation now drops the frontier; eligibility and the rewind handler both require a genuinely past/current-chosen node; old icons fade independently of beat position. After: matching `fix-after/` frames show frontier 3, meters 1,1,1, and all targets disabled on unanswered Batteries. Back plus Rewind, three initial targets, repeated earlier rewinds, and Next spam are checked in `fix-cheats.json` and `fix-exploits.json`. None skips a required choice. Longest-text selection still fills resources 8/8, however. See Cheats tried and Left open.

#### Should fix

1. **FIXED.** Before `fix-before/choice-read.png` and `before-choice-read.json` read the Batteries fact alone. Mission Control now voices the fact and both crew lines in displayed order on choice entry, Read, Radio again and Rewind. `fix-read-choices.json` checks 3 beats x 2 orders, 6/6 matching the buttons. Held-click main/side logs start every named transmission. `fix-after/choice-read.png` shows its Read caption. Ada's questions/reactions remain excluded; runtime and manifest contain the same 93 lines.
2. **FIXED for the picture defect.** Before `fix-before/night-000.png`, `night-010.png`, `night-111.png` show the same thriving background and squashed foreground. After `fix-paths/path-000.png`, `path-001.png`, `path-010.png`, `path-100.png`, `path-111.png` distinguish healthy, cold, thirsty and dark states at 1366x768. Leaves hang from bent stems, with shaded yellow blades and veins; cold alone has green drooping leaves and blue frost. Final Motion-off frames `fix-night-final/path-000.png`, `path-100.png`, `path-111.png` show immediate states: Light 3 versus 1 gives background brightness 0.90 versus 0.56 and saturation 0.85 versus 0.45; low Water lowers it further to 0.099 plus sepia; cold overlay is 0.8 versus 0. All eight meters/endings match independent arithmetic in `fix-path-validation.json`. The shared longest-text shortcut is not claimed fixed.
3. **FIXED.** Before: `fix-before/warm-680.png`, the 1366 map frames, `fix-before-phone/phone-map.png`. Six shared SVGs replace the battery/sun, moon, ice, wave, blanket and door glyphs in buttons, diamonds and Rewind. After: `fix-checks/warm-680.png`, `rewind-680.png`, `fix-after/double-rewind.png`, `fix-phone/phone-map.png`, `phone-warm.png` at 680x425, 1366x768 and a true 375x812 iframe. Map SVGs are 15x15. Choice icons and map dots are decorative; the path has list/listitem roles and accessible choice/rewind names carry the words.
4. **FIXED.** `before-job-first-sound.json` has only the job event after badge, Sound off/on and Crew re-entry. `after-job-first-sound.json` recovers the valid premise once. `fix-premise-at-start.json`, `fix-mission-first.json`, and `fix-main-voice.json` carry it into Start mission on badge-first and Mission-first routes. Frames: `fix-final/mission-final.png`, `fix-phone/phone-intro.png`. Crew Read also includes the premise without the stale badge instruction.
5. **FIXED.** Actual Audio fixture before: `before-clip-read.json`, glow false and stale caption. After: `after-clip-read.json`, glow true with exact Read text during playback and false after its 3-second clip completes. `fix-clip-event.json` proves the same event lifecycle. `fix-clip-interrupted.json` proves Sound-off Read stops on Motion and leaves glow false. Events follow V.playing; a small Read adapter follows the actual completion promise of kit playback, without an estimated glow timer. Silent WAV fixtures exercise clip control flow; no narration was recorded. Frames: `fix-final/`.

#### Polish accepted

1. **FIXED.** All three ending transmissions speak the story first, then their first reflection instruction, naming New mission or Rewind. `fix-paths/path-000.png`, `path-010.png`, `path-111.png` and the two held-click logs prove the order. Later endings omit the repeated how-to.
2. **FIXED.** Shared choice content says "Wrap the greenhouse in a blanket" in the button, accessible map/rewind name and spoken options. `fix-checks/warm-680.png`, `fix-phone/phone-warm.png`, `fix-read-choices.json`.
3. **FIXED.** `fix-six-reactions.json` records all 6 distinct in-role card reactions after their results. None enters runtime allLines or the voice manifest.
4. **FIXED.** A revisited unanswered choice adds "Say the new line in your own words. What will you tell me?" on Ada's card, unspoken. `fix-checks/rewind-680.png`, `fix-after/double-rewind.png`, `fix-phone/phone-rewind.png`, `fix-exploits.json`. Choosing replaces it with the result reaction.
5. **FIXED.** Notes explicitly name the three responding asks: choose a job prop, explain how the crew met the Moon problems, and judge which choice mattered with a reason. Talk about it includes the doors question. The revision invitation is also explained.
6. **FIXED.** Dialog return and corresponding fixed narration say "Back to the story". `fix-after/double-rewind.png`, `fix-phone/phone-map.png`; the phone label fits its 60 px target.
7. **FIXED.** `fix-after/crew-1920.png` and `fix-crew-spacing.json` at 1920x1080 show a 15 px prop/label gap and 14 px subtitle/badge gap. The grid starts lower; props retain label space while selected.

#### Settled calls

- Mission Control voices the crew options, never Ada. The broader solo-role question and Warmth B rewrite remain untouched.
- Ending pictures are stronger. How-to-before-story stays on beats 2 to 7; only endings change order.
- Immediate interruption, replayable job events and card/Motion interruption remain. Moon fact wording and all eight resource rules are unchanged.
- No new assessment, paid generation, uploads, commits or shared-file changes. Only the named tool and Scratch were written. `refine.md` and `refine/` were untouched.

#### Cheats tried

- Rewind Batteries, then try Water/Warmth without a new Batteries choice: formerly reached the invalid 1,1,3 ending; now blocked by eligibility and handler guards. Current unanswered Batteries is disabled too. Before/after rewind frames and JSONs prove it.
- Back from the ending to Batteries, then Rewind to any choice, or spam Next: remains blocked on the unanswered choice. `fix-cheats.json`, `fix-exploits.json`.
- Start a rewind at each of 3,4,6, then attempt later and earlier targets. Later skips fail; earlier targets restore and reduce the frontier again. First restored meters are 1,1,1; 3,1,1; 3,3,1. `fix-exploits.json`.
- Repeat the poor choice 10 times and alternate both buttons 10 times at each choice. Resources remain 1,1,1; 1,2,1; 1,2,1, never stack, and the other committed choice asks for Rewind. `fix-cheats.json`.
- Always left across all 8 shuffle configurations: full ending 1/8. Every meter matches the semantic choice. `fix-exploits.json`.
- **NOT FIXED: always choose the longest line without Moon science.** Full ending 8/8 across shuffle configurations. This is not learning evidence. The spec prescribes those lines and a revisable story with no mastery assessment; settled calls retain the content/resource rules. I did not add an assessment gate or rewrite choices beyond this Refine. This is why the meter blocker is not certified FIXED under the user's stronger condition.
- Badges assign replayable crew roles, not scores. No saved/best score, reward or mastery claim was added. Read and rewind openly provide teaching content as specified.

#### Voice walk

- Held 120 ms presses, 2 s gaps, default Sound: ready + Plant Keeper; premise + long night; next + greenhouse; choose + solar fact/options; Batteries A; water fact/options; Water A; lift ice; warmth fact/options; Warmth A; dust; full ending + reflection. All 12 transmissions start in order; each how-to starts once. `fix-main-voice.json`.
- Side path: corresponding B results; low ending + reflection; map; old story + warmth rewind + fact/options; Warmth A; dust; low ending without repeated reflection. All 17 transmissions start in order. `fix-side-voice.json`.
- Separate premise recovery and six Read-order cases pass. No Ada question, reaction or own-words invitation appears in the 93-line runtime/manifest set. Exact equality checked with `fix-final-lines.json`.
- A spoken log means the kit started the transmission; a subsequent tap may cut it, as Done when 5 requires. Browser voice quality is not certified. Actual clip control flow was tested with silent fixtures.

#### Engine changes wanted

- Existing: `kit/curio.js`, init Motion handler, optional memory-only preferences for literal no-storage tools.
- Optional: `kit/curio.js`, voice/read and speakOne, expose native Read's text and completion/playback callbacks for Audio and speech. That removes the local Read adapter; the current tool already follows kit playback completion.
- Existing audit issue: `scripts/audit_tool.py`, size iframe context discovery, add a same-origin iframe-window fallback. Separate actual phone-host checks succeeded. No shared source was changed.

#### Audit

Completed once, exit 0, within the 2400-second cap, Chrome 9911 and host 8715. Evidence: `fix-audit/audit.md`, `fix-audit-console.log`. All 68 audit frames were inspected. The audit was not repeated.

- **2 phone-probe leads:** iframe context discovery failed and therefore could not find the hint. Separate true 375x812 host frames in `fix-phone/` verify map, Warmth, revision, night and the long introduction; radio/card gap is 14 px and card/choice gap is 22 px in both choice states. Read speaks the actual context. Shared audit change is listed under Engine changes wanted.
- **1 real layout lead, FIXED:** the long Warmth rewind caption covered 3/9 choice sample points at 1366x768. Before: `fix-audit/state-warmth-revision-1366x768.png`. All choice layouts now reserve actual radio height. After: `fix-audit-followup/warmth-revision-1366.png` and `warmth-revision-680.png`; respective gaps 14 and 9 px, both centers unobstructed, full words visible. Coupled widths 1280, 1920 and 760 also have 14 px gaps and unobstructed centers. The matching `fix-warmth-revision-*-followup.json` files retain the numbers.
- **7 first-tap welcome leads:** Mission and the six job badges intentionally speak their own first action. The premise recovers at Start mission, Sound on or Crew re-entry, verified by the focused premise logs and main/side paths. No late, stale job-badge welcome was added.
- **9 quick-tap leads:** Crew, Mission, Motion and six job badges cut the preceding transmission. This is required by Done when 5 and the settled calls. Job events replay; their first combined how-to need not repeat. The five-held-click checks are clean for all 10 tested speaking controls, and Read is clean on quick taps.
- Final resize stress is clean: no exceptions or controls left disabled. The automatic Mission walk cannot enter without a job; the separate real-input paths supply Mission coverage.
- The audit snapshot predates the targeted spacing follow-up and an accessibility correction found during frame review: ordinary past nodes now say visited, rather than future/old. The final follow-up records all eight labels accurately. This changes no story resources or narration. The final default Crew and actual Mission were also re-shot at 1366x768 in `fix-audit-followup/`.

#### Left open

- Longest-choice shortcut. A full greenhouse cannot certify science understanding. Resolving the stronger condition needs a content/assessment decision outside this Refine's permitted scope.
- Both spec open questions remain untouched. Recording narration and shared Motion storage remain at their existing later-stage/engine boundaries.
- Corrected Scratch test errors: selector quoting in two voice shots and a duplicate local declaration in the first after-phone batch. Successful reruns provide the evidence. A targeted night batch and the first post-audit batch lost Chrome connections; smaller/allowed-port reruns passed. An optional interpreter lookup hit its 30-second cap and was abandoned; no dependency installation was needed.
- Bundle: 1,519,271 bytes. Standalone exploit run made zero external HTTP(S) resource requests. Successful drive batches had no tool-console errors. Authored files contain no em dashes. Final default Crew and actual Mission at 1366x768 are in `fix-final/`; final night Motion-off comparisons are in `fix-night-final/`.

All task Chrome debugging ports and host port 8715 were closed before report publication. Validation hashes, path data and final gaps are in `fix-validation.json`.
The shell cleanup had left three test hosts. `fix-process-cleanup.json` records their verified commands; `fix_cleanup.py` checked creation time and workspace before native termination. Final port checks confirm closure. The Scratch host helper now terminates its own process handle directly.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Moon Base Drama build handoff

#### Codex fix, round 1, 2026-11-06
This section supersedes the older review notes below. The current path frontier drops whenever Back or Rewind
invalidates choices. Rewind requires a node behind the current beat or a current choice; its handler guards this
as well as disabling the button. Old icons are independently faded, including an unanswered current node.

Choice content uses six shared inline SVG drawings on buttons, map diamonds and rewind cards. The map is an accessible
list with decorative dots. Options are voiced in the actual shuffled order after the fact, including Read and rewind.
The role premise can recover through Sound on or Crew entry and is carried into Start mission if still unheard.
The three endings speak the outcome before their first reflection instruction. Ada has six unspoken result reactions
and an unspoken invitation to revise dialogue in the child's own words after Back or Rewind.

Night rendering separately controls background light, desaturation, yellow hanging leaves, and cold-blue frost.
The painted backgrounds, healthy planter and all existing props remain. A ResizeObserver reserves the actual radio
height below choices at all sizes and card heights on phones. Compact choice captions keep the full fact and both options; their how-to and
rewind invitation are already in the visible hint and card. Large Crew badges have more subtitle and prop-label space.

Radio glow follows V.playing for events. Read uses a small adapter around Curio.say(text,true), whose actual promise
completion clears activeRead for both Audio clips and speech synthesis. Every operative action clears activeRead and
hushes the kit. No queue or audio engine is copied. Header Read and modal Read map use the same adapter. Read events
are retained in V.log. This is needed because the current kit does not expose native Read's completion or playing text.
All fixed Read forms and both option orders belong to L and voice/lines.json (93 matching lines). No narration was recorded in this fix.

The single final audit completed with exit 0 and 19 leads. All 68 frames were inspected. Its real new lead was a long
rewind caption overlapping choices at 1366x768; measured radio height now reserves that space at every choice size.
Targeted follow-up frames show 14 px separation at 1366x768 and 9 px at 680x425, with both button centers unobstructed.
The same follow-up verifies accurate visited/current/old/future accessible path labels, including ordinary nonchoice
beats. The audit snapshot predates these two small follow-ups; the audit was not repeated. Detailed evidence and
dispositions belong to polish.md.

The prescribed options still admit an always-longest-text route to full resources in all eight shuffle configurations.
No new assessment or content rewrite was authorized by this Refine. The report conservatively leaves its stronger
no-skill-pass condition open; full resources must not be represented as proof of Moon science understanding.

Current evidence and the final audit are under `_scratch/moon-base-drama/fix-*`. Read polish.md for verified outcomes.

#### Structure
`src.html` starts from the kit starter. Its permanent DOM contains the painted stage, six crew badges,
Mission Control radio, Ada's separate card, three meters, eight-node map, two choices and native rewind dialog.
Responsive CSS lays out actual pixels rather than scaling the whole board. Compact landscape keeps the
teacher's card beside the choices; phone controls use two rows. Art tokens appear once in the ART table.

JOBS, BEATS and L hold content. Ada's lines live only in BEATS and the card renderer. They never enter L,
`allLines()` or `voice/lines.json`. The voice manifest requests firm-captain / Alnilam. No speech was recorded,
as required for this Build; the kit currently uses available browser speech. The requested bank timbre awaits recordings.

`state.choices` contains active branch choices. `meterValues()` folds the three changes from the initial
1, 1, 1, so tapping again never stacks resources. Back or Rewind invalidates choices at and after its target;
`oldChoices` preserves their faded map icons. New mission resets story state and retains assigned jobs.
Mode changes retain the story. No story state is stored.

Each operative tap hushes narration on pointerdown, then acts on click. A revision guards queued event lines.
The tool uses `Curio.voice` with mode plus beat scope, `V.heard` for how-to lines, and the kit audio context
for 200 ms filtered radio noise. The radio caption follows active narration; Read never speaks Ada's card.
The round 1 fix section above describes the current glow and Read behavior.

#### Art
Fourteen generated paintings are in `art/*.webp`, with originals in `art/raw/` and full prompts in
`art/prompts.json`. The built-in image tool made them during this build. All were inspected after the
required free `art.py --rekey <name>` processing. The six job props, rover, ice and five settings match the
spec; an additional painted greenhouse planter gives the code-controlled droop a painted leaf layer.
SVG clips split its leaves from its tray. Meter transitions, rover arrival, ice floating, charging and
warmth effects stop with Motion off. The idle beacon stops too. Empty suits are equipment, with no people.

#### Spec decisions and ambiguities
- No explicit open questions appear in the spec.
- The explicit user instruction to stop when codex-report.md is written takes precedence over the build
  brief's early-report advice. The report is written last; evidence accumulated in Scratch meanwhile.
- The user requested the image tool, which takes precedence over the spec's local FLUX pipeline choice.
- Read on Mission and Radio again replay the current radio message, including a selected choice's result.
  Read on Crew speaks the current action hint. Neither speaks Ada's script.
- Both Mission entry and Start mission require a checked job. A premature Mission tap names the job action
  and focuses its first badge. Back at beat 1 returns to Crew; Next at beat 8 becomes New mission.
- A newly picked branch leaves later old icons faded until a new choice is picked at those beats. The new current
  choice replaces its old icon immediately, and active resources include only the new branch.
- The story map is a compact, noninteractive strip. Rewind opens the large three-choice map; unavailable
  future choices are disabled. Before any choice is visited it explains how to return instead of naming a disabled choice.
- The shared kit stores only its Motion preference. The spec's literal "nothing is saved" cannot be fully
  satisfied without a kit change. Notes disclose this; no classroom or story information is saved.
- The Sources temperature conversion is wrong: minus 130 Celsius is minus 202 Fahrenheit, not minus 208.
  The radio has no exact temperature, so no script correction was needed. The spec itself is unchanged.
- Cold review corrected the overbroad freezer dialogue to a home-freezer comparison, clarified daylight
  versus the full lunar day, and distinguished no breathable air from literally no atmosphere.
- This is a teacher-led role play, not a scored quiz. The supplied choice order and truthful teaching
  feedback remain. The meters show story resources, not physical engineering quantities.

#### Engine changes wanted
- `kit/curio.js`, `init` Motion handler: add an opt-out for persisted Motion preferences, so tools requesting
  no storage can keep that setting in memory. No shared files were changed.
- `kit/curio.js`, `voice` / `speakOne`: expose actual playback start/end callbacks for both recorded clips and
  browser speech, including Read, and expose Read's current text/completion. This would let radio tools attach
  crackle and glow to one playback interface and remove this tool's small Read adapter. The tool now supports
  recorded playback through that adapter and V.playing; the shared change is optional for this fix.

#### Verification and next workflow
Cold review changes: the first how-to is a prefix in its event transmission, chosen using V.heard across
the finite guided keys. This keeps the instruction and fact in one real utterance at a two-second tap
pace. The transmission is an event, so later job/beat/result taps still speak, without repeating its how-to.
The voice manifest includes these fixed combined transmissions as well as their individual lines.

Choice positions are sampled once per mission and retained across rewinds. State stores semantic choices,
not button positions. A committed choice can only change after Back or Rewind. Opposite taps leave every
meter unchanged and name Rewind. These are story outcomes, not an assessment of a child's knowledge.
The rover now brings a visible ice load after a water choice, with a smaller load for finding it late.
Compact screens retain battery and warmth effects. New mission from the map restores focus to Next.
On phones, response art sits to the right of the beat label and the ending planter sits above Ada's card,
so the changing plants and tray remain visible instead of disappearing behind the script.
The longest first-beat caption also has a clear gap below Ada's card. This phone-only spacing repair was
made after the review audit's failed iframe-context probe and rechecked in a real 375 px host.
Read map is available inside the native modal and speaks its own instruction, never a covered story beat.

#### Sensitivity
Fictional crew roles and Moon science, with no cultural, religious, Indigenous or hard-history representation.
The class supplies the people in this teacher-led drama; the paintings deliberately show empty equipment.

#### Original build verification
Scratch contains numerical recomputation, all eight real-click path results, all required viewport frames,
phone host checks, keyboard and narration logs, Motion off and grayscale frames, and the final audit output.
The full audit finished in 1,384 seconds with 22 leads. Compact hints and Back focus were repaired and
checked separately afterward. The map state's keep region now checks its dialog rather than the inert
background controls. Missing Crew welcomes after a job or Mission tap are intentional: the spec makes
them stale. Quick repeated Crew or Motion taps deliberately cut speech, and the kit marks a welcome
heard when it starts. The full welcome remains in the Crew radio caption; no stale welcome is replayed.
The audit was not rerun after these targeted repairs. `audited-bundle.html` in Scratch preserves its input.
`codex-report.md` records the audit disposition and any remaining limitations. A cold review is next.
Build only: no commits, branch operations or polish round. Only this tool and its Scratch folder were written.

#### Cold review verification, 2026-11-05
The review audit ran once with the 2,400-second cap and completed with exit 0. Its 18 leads are two
iframe-context probe consequences, seven intentional first-tap welcome skips, and nine intentional
quick-tap interruptions. Five-click repeats, layout/target checks, Motion off and resize stress were clean.
Its automatic Mission walk stays on Crew because a job is required. Separate real-input Mission walks
cover all eight outcomes, every resource sweep, all rewinds, replay, Sound-off Read and keyboard controls.
The 59-line manifest matches runtime allLines exactly. No story state is persisted.

The failed iframe probe was covered with real held input at 375 px via host port 8755. That follow-up
found a small first-beat card/radio collision. Only the phone spacing changed after the audit, with Crew,
night and the longest first-beat message re-shot. The minimum measured gap is 3.625 px; phone job badges
remain 172.5 px high. The audit input is preserved in `_scratch/moon-base-drama/review-audit/host/tool.html`.
All 64 audit frames were inspected. Other current evidence and the final validation manifest are in Scratch.

Audit reader improvement wanted, outside this tool's write scope: `scripts/audit_tool.py`, `Audit.size`,
needs a fallback when child-frame execution-context discovery returns none. A same-origin iframe-window
probe worked in the separate drive.py host tests. No audit, kit or other shared source was changed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
