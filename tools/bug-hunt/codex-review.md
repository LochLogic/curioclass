# Codex review: bug-hunt
## Played
Cold Grade 8 play preceded all builder files: a real hunting round, History, Explain and all eight story stops; then the full fourteen-round Hunt with held input.
The bark, bird and reversal of camouflage are strong. History makes the population lesson visible. Explain is much easier to guess than to reason through.
Root was S:\CurioClass-codex throughout. No commits. Authored files stayed in tools/bug-hunt/ and _scratch/bug-hunt/.
## Findings fixed
Native checks and before/after frames are indexed in _scratch/bug-hunt/review-gallery-index.json; named voice and cheat logs below supply the reproductions.
- Blocker, general, Run prediction: fixed random seed exposed the next result through replay. Reset and History now start fresh trials; explicit test seeds still work.
- Blocker, general, Hunt Pause: blur still revealed a dark moth's location during a frozen clock; a native resume-and-peck caught it. Paused rendering now omits moths while retaining bark, bird and population state.
- Should fix, general, Real story / Explain: old speech continued over a different scene or answer. Feedback interrupts obsolete speech while preserving Read priority.
- Should fix, general, wrong-card feedback: repeated taps could cut the one allowed explanation short. The same refused card now keeps its narration playing.
- Should fix, general, Explain: chip instructions could be dropped before the first chip tap. Correct feedback and the next action now share one how-to line.
- Should fix, general, Run: active playback still told students to press Play. Hints now name the actual Pause control.
- Should fix, general, main-path Run voice: Play, Step and History now interrupt the obsolete welcome before its Play instruction can run over active playback; History's own line follows immediately.
- Should fix, general, Hunt voice: a first Pause or a return to paused Hunt could welcome students by telling them to peck. It now says Resume; next-generation speech is invalid while paused.
- Should fix, general, Run sample: the title obscured the first moth row. All forty moths now sit below the label.
- Should fix, general, 375-pixel layout: Run controls clipped and Bars pushed them farther down. Bars and Line share the plot; controls fit through Reset.
- Should fix, general, phone prediction regression: Predict now opens Line; returning to Bars gives a valid Line instruction, dropped when stale. Locking the pin stops obsolete how-to speech.
- Should fix, general, phone feedback: kept Explain's original stage height and tightened the cards so a refusal remains visible with all three choices.
- Should fix, general, phone Hunt: the histogram fell below the viewport. Rebalanced field, timer and graph; moved the tip below them, retaining the painted field.
- Polish, general, breeding: strengthened the flattest transition with the actual pale/dark parent counts, retaining pulsing survivors and the newborn fade.
- Polish, general, art: repainted carbonaria with clearer body shading and wing detail; preserved its calibrated darkness and the rest of the set.
- Polish, general, tint canvas: marked its readback use explicitly, removing the warning exposed by the calibration check.
## Findings left
- Blocker, general, Explain: blind enumeration opens writing; the correct card is also conspicuously longest. Cold and post-fix native attempts confirmed this.
  The spec prescribes both the exact cards and retry-to-correct flow. Changing that gate or its wording needs a spec decision, so CODEX-REVIEW section 3 forbids improvising it here.
- Should fix, general, statistical acceptance: the written model does not meet the spec's quoted Hunt and Birds-off percentages. Exact rules retained; measurements below.
- Should fix, general, no-eaten explanation: the prescribed "every moth bred" overstates a model with 30 survivors but only 29 local young after the incomer replaces one.
  Run likewise has 200 survivors and 196 local young. Seed-1 parent tracing confirmed a missing parent in both cases; see review-parent-coverage.json.
- Polish, general, low-peak ending: the prescribed chance wording can understate a student's deliberate reverse selection. It remains the specified ending, not an earned success claim.
## Break it
- Hunt counter: bare-bark taps, rapid repeated taps and a blind 135-point grid sweep. The lockout held; the grid caught 2, not 15. No saved best score exists.
- Pause / mode escape: clock delta 0 over 2.5 seconds while paused; moths hidden after fixing the visible blur silhouettes. Returning to Hunt preserves the pause rather than granting scouting time.
- Population meters: 30,800 review-run snapshots of the shipped model conserved 30/200 moths; histogram dark bins equaled the line's numerator, with legal inherited copies.
- Hunt behavior, 200 seeds each: careful peak 15+ on soot 75.5%, final at most half that peak 89.5%; idle peak 1.5%, two-eaten masher 2%, random fifteen-eater 9.5%.
- Run, 50 seeds: History rose above half on soot and fell below half by generation 55 in 50/50. Birds off stayed below 25% in 40/50; both toggles off in 48/50.
- Slider sweep 0 to 100 without advancing: generation and dark count stayed 0. Extremes 0/100, clearing 50 and generation 120 worked; the cap disables Play and Step honestly.
- Prediction: real drag set generation 25; Step and off/on toggles left it locked at 25. Three new History trials differed, so observing a replay no longer reveals an exact future.
- Live History takeover: real Bark drag changed the next cohorts to darkness 50 while playback continued; the current band and hint agreed.
- Explain: both misconceptions refuse with their own reasons. All-options guessing still opens the boxes, an unresolved spec-constrained blocker, not excused as "only teaching."
- Evidence chips: no-data chips disabled; saved text survived a fresh load. Writing and Copy award no mastery or completion score. Generated counts were compared with the actual Hunt records.
## Voice walk
Held pecks at a 2-second pace, twelve per round with the full 25-second timer, through all fourteen generations and both narrated story cards; then Explain, History and Real story.
Heard in order: breed, sootCard, nextGen, cleanCard, huntEnd, welcomeExplain, cardWrongA, writeEvidence, welcomeRun, history, welcomeStory, stop2, stop7, stop8.
The first hunting tap skipped welcomeHunt, allowed by BASELINE 16; its instructions remained in the hint and Read. Both story-card narrations finished before Continue.
The browser reverted to a compact viewport between the two bounded Hunt batches. The compact writing path was rechecked using its actual Next buttons.
Main and targeted logs: _scratch/bug-hunt/review-main-phase-*.json, review-compact-writing-path.json, review-read-priority.json and review-repeat-*.json.
| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| breed / nextGen / each mode how-to | how | once | once each |
| miss, five held taps | how | 1 | 1 |
| refused card A, five taps in one visit | event, spec once per card | 1 | 1 |
| same story stop, five taps | event | 5 | 5 |
Sound-off Read worked; mode changes released Read; stale story events did not speak over a later scene. Fixed strings matched allLines and the 31-line voice catalog.
## Facts checked
- Inherited variation, dominance and selective predation: [Cook and Saccheri, Heredity 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3668657/).
- Cortex-region DNA insertion and inferred date about 1819: [van't Hof et al., Nature 2016](https://pubmed.ncbi.nlm.nih.gov/27251284/). This is an inferred origin, not a witnessed mutation.
- First recorded dark Manchester moth in 1848; near-city dark frequency about 98% by 1900: [Arizona State University](https://askabiologist.asu.edu/games-sims/peppered-moths-game/natural-selection.html).
- Manchester's 98% by 1895: [Butterfly Conservation](https://butterfly-conservation.org/moths/why-moths-matter/amazing-moths/peppered-moth-and-natural-selection), corroborated by [Grant and Wiseman 2002](https://pubmed.ncbi.nlm.nih.gov/12140267/). No annual series was invented.
- Soot, pollution and lichen loss; Kettlewell's 1950s polluted/clean experiments: Cook and Saccheri, above, and the original 1955/1956 experiments they cite.
- Britain's 1956 smoke-control law: [Clean Air Act 1956, chapter 52](https://www.legislation.gov.uk/ukpga/Eliz2/4-5/52/enacted). Enactment is distinguished from later implementation.
- Dark-form decline since the 1960s/1970s: [Cook et al., Biology Letters 2012](https://pubmed.ncbi.nlm.nih.gov/22319093/).
- Michigan's parallel decline and absence of detectable local lichen change: [Grant, Owen and Clarke, Journal of Heredity 1996](https://academic.oup.com/jhered/article-abstract/87/5/351/816056?login=false).
- Majerus's Cambridge-area study and greater dark-moth predation: [Cook et al., original paper](https://mallet.oeb.harvard.edu/sites/g/files/omnuum6606/files/malletlab/files/609.full_.pdf).
  Independently summed its six release rows to 4,864. Releases were 2002-2007; the stop's 2001-2007 span includes baseline observations, not seven release years.
- Counts, mutation rates, incomers, timings and darkness formulas are explicitly game assumptions from the spec. They are not field estimates.
- Bark darkness remeasured 20.114 / 50.151 / 85.230; six rendered moth targets were within 0.008. Contrast: ink/paper 12.92, muted/paper 5.63, white/brand 6.39.
## Sensitivity
English industrial/scientific history: check credit to named researchers, illustrative rather than documentary scenes, and the distinction between demonstrated bird selection and disputed lichen contribution.
No Native, religious, personal-body or hard-history content is introduced. No people appear; all twelve assets are marked people false. Woodland and town exteriors do not require a token worker figure.
## Flattest moment left
The last clean-bark rounds repeat the same hunt after the lesson is visible. Their recorded population remains meaningful, but no extra mechanic or topic was added beyond the spec.
## Graphics
All twelve images inspected, including keyed cutouts, 54-pixel moths, 130-pixel bird poses, bark in play and all four story scenes. One carbonaria redraw via the imagegen skill's built-in edit path.
Kept the field-notebook palette, rich oak textures, painted landscapes, bird and animated graphs. Compared existing Beat Lab and Snowy Mail Route bundles without rebuilding them.
Art prompt: tools/bug-hunt/art/prompts.json; final cutout: art/bh-moth-carbonaria.webp; original retained in Scratch. Final offline bundle: 2,056,608 bytes (2008.4 KiB), below 2 MiB.
## Audit
One audit completed, exit 0, within the 40-minute limit: Chrome 9961, host 8765; 39 leads, 83 frames, in _scratch/bug-hunt/review-audit/.
- Confirmed and fixed: paused moth silhouettes and the Pause welcome mismatch; native paused/return paths now show no moths and say Resume.
- Intended overlaps: notebook labels over the canvas and modal covers over inactive field text. The prediction readout occupies clear graph space. Kept after viewing.
- Dropped breeding how-to: fixture skips the breeding beat immediately; the held-input main path spoke it. Quick mode/welcome cuts are allowed by BASELINE 16.
- Explain table pairs cached labels with newly shuffled positions; text-targeted native checks confirmed each feedback matches its actual card.
- Phone audit unavailable: port 8765 served an earlier tool-folder helper, so audit host URLs returned 404. Its phone "nothing new" is not a clean result.
- Separate 375-pixel tests covered every mode, both Run plots, unlocked/locked prediction, Hunt Pause/cards/end and Explain refusal/writing.
- Audit snapshot precedes final phone and voice repairs. Those received targeted re-shoots and held-input voice checks, without a second audit or review round.
Also viewed 28 mode/size frames across all seven STANDARDS sizes; checked calm, grayscale, keyboard, extremes and resized actions. Audit resize stress had no exceptions or stranded disabled controls.
Wave checks covered focus retention, load focus, targets, visible choices, hints/Read, state-matched speech and matching graph counts. Explain remains the named no-giveaways failure.
Evidence index: review-gallery-index.json; numeric checks: review-numbers.json and review-parent-coverage.json; later voice/phone logs: review-*-voice*.json and review-phone-predict-branch.json.
## Left open
The spec-constrained Explain blocker and quantitative/parent-representation conflicts above prevent an unqualified PASS. No model tuning, extra assessment, new feature or kit change was made.
No recordings were created. Browser fallback speech was enabled; muted timing/log checks cannot judge narration timbre or pronunciation by listening.
All Chrome ports 9960-9967 verified closed. Windows denied taskkill for the earlier HTTP helper PID 55144; port 8765 may remain occupied. Temporary tool host removed; cleanup evidence: review-cleanup.json.
Initial short read commands completed before the explicit timeout wrapper was installed; subsequent bundles, drives and audit were process-bounded. No commits.
