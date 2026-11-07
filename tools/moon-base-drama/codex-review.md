# Codex review: moon-base-drama

## Played

Cold K-2 crew/teacher walk before opening builder reports or source: all weak choices, ending, then a changed battery branch. Strong painted base and props; the class performance makes this a drama.
One review pass, scoped fixes and targeted rechecks. Root verified as `S:\CurioClass-codex`; no commits.

## Findings fixed

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

## Findings left

No remaining blocker or should-fix within this tool's authorized scope. Recording and shared-kit limitations are under Left open. The separate narration recording stage remains outside this brief.

## Break it

There is no score, quiz, reflection completion gate, best score or saved achievement. Meters are explicitly fictional resources, not knowledge scores or engineering measurements.
Before fixes: repeated taps did not stack dots, but both-option sweeping could replace a weak choice, and all-left reliably filled every meter.
After fixes, real input: five wrong/right alternations per meter stayed at 1/1/1, 3/2/1 and 3/3/1 respectively; all-left gave 1/2/3 and a low ending. Rewind restored 1/1/1, 3/1/1 and 3/3/1; New mission kept jobs and focused Next. Eight final held-click paths match the independent outcomes below. Empty Start and the Mission-tab bypass both remain on Crew after the gate repair; unanswered Next remains at beat 3. Keyboard-only input reached beat 8.
Independent eight-path computation: AAA 333, AAB 331, ABA 323, ABB 321, BAA 133, BAB 131, BBA 123, BBB 121. One full ending, three two-full endings, four low endings.
Production logic also passed 62 DOM-stub checks: every meter's five alternating attempts, eight endings, Back, all rewind targets and eight observed order variants. This supplements browser evidence.
Guessing can succeed by chance in a two-choice drama. Rewind deliberately supports revision; no screen claims that a glowing greenhouse proves mastery. The supplied facts scaffold the crew's choices; children give their reason aloud.

## Voice walk

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

## Facts checked

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

## Sensitivity

None: fictional Moon crew and science, no cultural, religious, Indigenous, hard-history or body instruction. Empty suits are equipment; the real class supplies the people. No painted person needs a people flag.

## Flattest moment left

Brush off remains a static airlock while the class mimes dust removal. The crew's performance carries it. The formerly flat water answer now has a loaded-rover payoff.

## Graphics

All 14 final assets inspected: six prop cutouts, five settings, rover, ice and planter. One crater replacement plus one targeted revision; other strong paintings kept.
Built-in image tool, final `art/raw/ice-crater.png`, required free `art.py --rekey ice-crater`, final `art/ice-crater.webp`; full prompt in `art/prompts.json`, original retained in Scratch.
No missing art tokens/files. Bundle 1,509,808 bytes; art 1,080,402 bytes. Nothing removed for size. Compared with existing Snowy Mail Route and Beat Lab bar frames.
Contrast: white/brand 9.08, brand/paper 8.17, ink/paper 14.92, muted/paper 6.00, ink/Ada 15.63, all AA for text shown.
Inspected cold play, all seven desktop/preview sizes, changed scenes at 680/1366/760, all eight initial endings, modal and voice frames. Phone Crew, battery, water, night and map checked at a real 375 px iframe; the two phone repairs re-shot. Real keyboard-only R, Escape and A shortcuts also passed.

## Audit

Ran once, last, with a 2,400-second limit: completed, exit 0, 18 leads. Full result: `_scratch/moon-base-drama/review-audit/audit.md`.

- Two iframe leads: the audit could not attach to the child context, so it also reported no hint. Direct 375 px host checks passed, including Read and the longest message. This follow-up found the final phone spacing collision; repaired and re-shot Crew, night and first beat.
- Seven welcome leads: six badge taps and a guarded Mission tap speak their own fitting line. Skipping the unmarked welcome follows the spec and first-tap rules; no late welcome follows them.
- Nine quick-tap leads: Crew/Motion welcomes, the guarded-entry how and six first-job transmissions are cut by the next tap. This is the explicit interrupt-on-any-tap rule; how-to lines are marked when they start. Read can repeat the current instruction.
- All five-click repeat checks clean; no console errors, undersized targets, desktop clipping/overlap, focus failures, infinite calm animation, resize exceptions or stuck controls. All 64 audit PNGs inspected through six labelled sheets.
The job gate means the automatic mode walk stays on Crew. Separate eight-path, main-voice, replay and keyboard runs cover Mission. The phone-only spacing fix followed the audit; affected 375 px states were rechecked. No second audit was run. Both bundle hashes are preserved in `review-validation.json`.

## Left open

No audio recorded: browser speech works; firm-captain/Alnilam timbre and classroom audibility await the separate recording workflow.
The shared kit remembers Motion on this device. Story/jobs are not saved or sent. Kit persistence opt-out and recorded-playback glow callbacks remain in handoff; shared source files unchanged.
Unattended decisions followed spec/baseline without questions. No mode, topic, score or kit feature added. Science corrections and ordinary choice-order/commit behavior support the existing lesson.
Process note: the first two read-only bootstrap commands were not timeout-wrapped; they completed immediately. All later commands used the bounded runner. Review browsers/servers are closed; temporary host.html removed.
