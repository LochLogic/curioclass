# Codex report: moon-base-drama

## Built
- Teacher-led K-2 drama with Crew and Mission modes, six painted job badges, eight story beats and three resource choices.
- Ada's readable script card, separate Mission Control narration, radio crackle and captions, story map, Back and Rewind.
- Branch changes restore earlier resources, preserve faded old choices, and change the night greenhouse ending.
- Painted lunar scenes, rover arrival, floating ice, charging battery, warmth feedback, lamp glow and a drooping painted leaf layer.
- Required source, draft metadata with stage built, teacher notes, 33-line voice manifest, audit states, art prompts and handoff are present.
- Final offline bundle: 1,555,762 bytes, about 1,519.3 KiB. Build only; no commits, branch operations or polish round.
- Working directory verified as S:/CurioClass-codex. Project writes stayed in this tool and its Scratch folder.

## Numbers check
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

## Feel check
Played complete perfect and imperfect missions, all three rewind destinations, and a keyboard-only complete mission.
- Best moment: arriving at the greenhouse after changing the story, with the crew's own map icons, three full meters and glowing lamps.
- Flattest moment 1: the first ending differed mainly in words. Added a separately painted planter with code-controlled leaf droop and count-dependent lamps.
- Flattest moment 2: choices initially changed only dots. Added charging and warmth/air-loss feedback, and moved the rover clear of the choices.
- Props visibly grow on assignment; the radio responds immediately. Teacher-controlled pacing leaves room for spoken answers and mime.
- This sustains a class drama through their performances and revisions. Clicking through alone is much shorter than the intended 20 to 30 minutes.
- Bundled bar copies in Scratch and opened Snowy Mail Route and Beat Lab before implementation.
- Looked at `feel-compare.jpg`: Moon Base Drama beside Snowy Mail Route. The painted setting, foreground plants and practical lights meet the visual bar.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
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

## Art made
- 14 images: five settings, six job props, rover, ice block and the additional foreground planter. All have no people.
- Total WebP art: 1,117,298 bytes, about 1,091.1 KiB. Final bundle: about 1,519.3 KiB, below 2 MB.
- Built-in image tool; full prompt set in `art/prompts.json`, raw originals in `art/raw/`, final assets in `art/*.webp`.
- No redraws required. Rekeyed cutouts with hole removal and despill after seeing a green rover fringe. Added the planter to replace the plain code leaf art.
- Generated-image credit is in source, notes and tool.draft.json. Every painted asset is used.

## Art still to paint
None. Empty hanging suits are equipment; no people, faces or body parts were generated.

## Engine changes wanted
- `kit/curio.js`, init Motion handler: allow an in-memory-only preference for tools whose spec requires no storage.
- `kit/curio.js`, voice and speakOne: expose playback start/end callbacks for consistent radio glow and crackle with future recorded clips.
No engine files were changed.

## Left open
- No narration was recorded, as instructed. The manifest requests firm-captain / Alnilam, but current playback uses browser speech; that timbre and audible classroom quality remain unverified.
- Literal no-storage compliance needs the kit option above. Only its shared Motion preference is persisted.
- The exact supplied freezer line remains scientifically overbroad; teacher notes qualify it. The owner can revise the script in the next review.
- Final targeted repairs have not had a second full audit. A cold review is the next workflow step.
- Temporary host.html removed. All test Chrome processes and servers started for this build are closed.
