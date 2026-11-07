# Codex report: illusion-lab

## Built
Built 2026-11-07 in `S:\CurioClass-codex`. Build only; no commits, deployment, shared-file edits or polish round.
The single offline deliverable is `illusion-lab.html`; edit `src.html` and bundle with `CURIO_DRAFT=1`.
Six full station state machines, Do/Compare/Why, a painted Bench, first/latest Notebook table, Eyewitness, keyboard input,
Motion off, real measurement timing, and kit narration are implemented. Metadata is beta / built.
All work is confined to `tools/illusion-lab/` and `_scratch/illusion-lab/`. Chrome used only 9990 through 9997; host 8795.
Source, notes, draft metadata, 17-line voice manifest, 20-state audit manifest, prompts, WebPs and handoff are included.
No audio was recorded. The bundler's missing-recording notices are expected; browser speech is the kit fallback.

## Numbers check
Independent computation: `_scratch/illusion-lab/recompute.py` and `numbers.json`, made before implementation.
- Step edge: k=0 gives 0.80/0.30; k=0.2 gives edge 0.69/0.19 and interior 0.64/0.24;
  k=0.4 gives edge 0.58/0.08 and interior 0.48/0.18. Patch edges 0.36/0.24, interior 0.30 on both surrounds.
- A/B canvas samples are exactly 110, then 121. Rod/cone ratio 92/4.6 = 20.
- 560 ms image + 160 ms blank = 720 ms per alternation, 1,440 ms per full A/B cycle; 1.3889 blanks/second.
  The spec's phrase "720 ms cycle" means a half-cycle. Timeout is 83 alternations, approximately 60 seconds.
- Example illusion calculations give 20% and 15%. A 100,000-start unmoved simulation averages -0.0135%, SD 18.91%; movement is required.
- Absolute four-percent hit-box padding gives 1.68% to 8.40% of the frame, before moved-position unions,
  rather than the spec's 0.8% to 6.2%. Three uniform guesses with kind guessing give approximately 1.67% to 8.17%.
  Kept the specified geometry; do not repeat the spec's smaller chance claim. Actual alternation and three-miss limits also apply.
- 32/14 = 2.2857; the card reports the original percentages instead of a misleading rounded risk ratio.
  69% of 375 is 258.75 because the published percentage is rounded; no invented integer count is shown.
- All adjacent letter trigrams share zero letters. Familiarity with every possible acronym cannot be guaranteed.
- Accent contrast: panel 7.78:1, secondary 7.36:1, stage 6.82:1; button ink 8.53:1, stimulus 12.08:1.

## Facts checked
Sources are also in `notes.md`; facts describe their samples and models, not a student's ability or a diagnosis.
| Student-facing fact | Named source and verification |
|---|---|
| Receptors, transduction, bipolar/ganglion cells, optic nerve, thalamus and cortex; rods in dim light, cones in color/detail | [OpenStax Psychology 2e, 5.3](https://openstax.org/books/psychology-2e/pages/5-3-vision). Path is explicitly simplified. |
| About 92 million rods and 4.6 million cones; approximately 20:1; counts vary | [Curcio et al., 1990](https://pubmed.ncbi.nlm.nih.gov/2324310/), sample averages. |
| Lateral inhibition, Hartline's horseshoe-crab work, contrast | [Rockefeller University history](https://centennial.rucares.org/index.php?page=Math_Neurophysiology_Vision), Hartline Nobel lecture and Purves as cited in the spec. Model arithmetic checked separately. |
| Muller-Lyer origin in 1889, angle dependence, practice/feedback decrement | [Dewar, 1967](https://www.appstate.edu/~steelekm/classes/psy4215/Documents/Dewar1967-muller-lyer.pdf), [Brosvic and Finizio, 1995](https://pubmed.ncbi.nlm.nih.gov/7567409/), origin corroborated by the 2025 review below. |
| Segall, Campbell and Herskovits' cross-cultural results and disputed building-corner explanation | [Amir and Firestone, 2025](https://perception.jhu.edu/files/PDFs/25_MullerLyer/AmirFirestone_MullerLyer_2025_PsychReview.pdf), discussing the 1963 study. Presented as disagreement; no societies ranked. |
| Identical gray, local contrast, shadow inference; Adelson 1995 | [MIT checker-shadow demonstration](https://persci.mit.edu/gallery/checkershadow/), plus Adelson 2000 cited in the spec. Generated checkerboard pixels independently probed. |
| Flicker masks change motion; attention and central/marginal interest | [Rensink, Vision and Attention](https://www.cs.ubc.ca/~rensink/publications/download/Vision&Attention-RR.pdf). Original scenes are not a normed stimulus set. |
| Approximate 80% at 3 seconds and 10% at 18 seconds with rehearsal prevention | Peterson and Peterson 1959, as sourced in the spec. These are approximate historical endpoints, not a fitted curve or a promised personal result. |
| Strong first trial and proactive interference; release after category change | [Keppel and Underwood, 1962](https://www.sciencedirect.com/science/article/pii/S0022537162800231), and Wickens 1963 as cited in the spec. Digit switch is a classroom demonstration. |
| Ebbinghaus 1885; fast then slower loss, a different task and measure | [Murre and Dros, 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644). |
| Encoding, storage, retrieval and reconstructive memory | [OpenStax Psychology 2e, 8.1](https://openstax.org/books/psychology-2e/pages/8-1-how-memory-functions) and DRM paper below. |
| Lure recall 40% with 12-word lists, 55% with longer lists; feeling of remembering need not imply accuracy | [Roediger and McDermott, 1995](https://psychnet.wustl.edu/memory/wp-content/uploads/2018/04/Roediger-McDermott-1995_JEPLMC.pdf). Their spoken lists differ from these original visual lists; on-screen comparison says so. |
| Speed estimates about 40 versus 34 mph; glass 32% versus 14%, one week later, no glass present | [Loftus and Palmer, 1974](https://stanford.edu/class/psych205/papers/Loftus-Palmer-1974.pdf). Corrected the spec's implication of one group: speed is experiment 1, glass is experiment 2 with different participants. Exact speed means are 40.5 and 34.0. |
| Mistaken identification involved 69% of historical 375 DNA exonerations, 1989 to 2020 | [Innocence Project historical dataset](https://innocenceproject.org/dna-exonerations-in-the-united-states/). Explicitly not all witnesses, convictions or a current case total. |

## Break it
44 earlier functional assertions passed across perception, actual memory timings, persistence and adversarial paths;
120 post-audit assertions passed, with zero exceptions. Additional native drag, keyboard, endpoint, phone and voice checks are saved in Scratch.
- Lines: unmoved Lock refused. Random starts stay hidden; at least three total units of adjustment are required.
  Dragged to a clamp and tried Lock: trial replayed, no row saved. Eight immediate endpoints cannot set a saved best.
  A rhythmic small move can produce a poor observation, not a perfect-match award; no accuracy badge or leaderboard exists.
- Shadow: unmoved match refused; minimum three gray steps required. Keyboard clamp submissions refused, no row saved.
  Exact A/B pixels were checked off the letter glyphs; Bridge and Hide scene keep shared gray unchanged.
- Eye: prediction is a recorded hypothesis, not a correct-answer score. Sweeping the slider alone cannot finish;
  all seven pathway stages and all three patterns at k=0.4 are required. Output is hidden before prediction.
- Change: wrong location and wrong kind each add a miss and resume the clock. Three misses produce Not found.
  Found a real cheat: a lucky guess from only the first picture could count. Fixed it: at least one actual alternation is required;
  re-tested premature correct-location guesses and observed-flip finds. Repeated completed scene sets are unsaved practice.
  Actual padded hit areas are larger than the spec's chance calculation; those odds are documented, not concealed.
- Count: tested no counting, wrong counting and rapid repeated taps. Nonresponses expire; sub-250 ms answers are rejected.
  Counting below 70% gives hollow points excluded from delay averages. Trial 1 and digit trial stay separately marked.
  A student can rehearse or use paper outside the app; the tool explains rehearsal control and makes no standardized assessment claim.
- Words: tested all Seen, all New, empty free recall, duplicate/plural variants, restarts and fast recognition.
  All Seen exposes 5/5 unrelated false positives; all New exposes 0/6 studied hits. Neither receives a success award.
  Seen requires Picture it or Just know. Replayed lists are marked seen twice with readable muted styling.
  Theme words are not named before the lists; the recognition lure must appear as an ordinary unmarked test item.
- Notebook: first remains unchanged after another run; latest and run count change. Reload preserves both.
  Cancel preserves records; Yes clears them across reload. Unfinished work cannot replace a completed record.
- Why/Eyewitness: reading or visiting earns no accuracy check. Eyewitness's question is conditional, because not everyone reports a false word.

## Voice walk
Native held clicks (0.12 s), two-second gaps, browser speech timing and `__tool.vlog` were used.
Main path: Line Lengths -> eight adjustments -> Compare -> Why -> Notebook: llHow, llDone, nbHow start in that order.
Side path: Shadow Squares (ssHow, ssB) -> Eye (eyeHow, eyeSlide) -> Change (scHow) -> Count (cbHow) -> Words (wlHow)
-> Notebook (nbHow) -> Eyewitness (ewHow, then Read). Recognition uses wlTest; full change run uses scKind and scNoGap.
Entering a measurement hushes the current line immediately; long instructions may be cut by a student's next measurement action.
No voice starts during a measurement. Read and explanation tabs are disabled while measurement runs.
The final seven-scene flicker walk confirms scNoGap starts once and finishes whole before scene 7; no speech starts inside any flicker interval.
A minimum reading window plus current voice/queue guard prevents Sound or Read from shortening the no-gap gate.
The formerly dropped eyeSlide now starts immediately; consistent inhibition changes no longer cut eyeBands.
llDone is an event and starts again after each new completed run; two-run post-audit assertion passed.
Station-first taps use their own how-to and suppress a late generic welcome, per BASELINE decision 16. Bench-first tap speaks welcome.
Fixed entry lines naming disabled Lock or Spotted controls. Their instructions appear in the live hint only when enabled.
Evidence: `voice-flicker.json`, `post-audit/voice.json`, `latest-voice-main.json`, `latest-voice-stations.json`.

## Feel check
Best moment: Bridge joins squares that still look different into a visibly continuous gray, tying a personal setting to a physical reveal.
Later rounds change fin angle/control, true gray, retinal pattern, scene and change kind, distractor delay/category, or recall versus recognition.
Two flattest build moments were the clipped compact Bench and floating-looking change objects. Rebuilt the short-screen grid;
repainted a shelf and bare wall so the plant and frame belong in their scenes. Both final composites inspected at 1366x768.
Compared the Bench frame beside the existing Beat Lab and Snowy Mail Route bundles. Kept their standard of visual specificity,
while using an orchid-accented observation lab, painted scenes and deliberately neutral experimental stimuli.
No decorative art is added inside exact-value line, gray, retinal or memory stimuli. Graphics support the experiments' teaching.

## Done when
1. **PASS**: at 1366x768 the stage dominates every Do view; required controls fit. Short screens use two-column navigation,
   controls before hints and a bounded stage. All seven desktop sizes plus actual 375px iframe checked.
2. **PASS**: eight shuffled line trials, three angles and two controls; no visible numeric readout before Compare;
   unmoved/clamped submissions refused or replayed. Compare labels 45, 90, 135, Controls and zero reference.
3. **PASS**: exact 110/121 A/B probes; all four matches; Bridge and Hide scene tested.
4. **PASS**: output hidden before prediction; independent arithmetic and browser values match the specified edge/interior/patch outputs.
5. **PASS**: 1.3889 blanks/second maximum schedule; Spotted freezes immediately, including a blank-phase tap;
   wrong kind increments a miss; Motion off defaults to manual Flip. Actual alternation required for a find.
6. **PASS**: all ten trials completed at real timings; counting required; hollow trials excluded; first/digit markers and approximate endpoints shown.
7. **PASS with documented wording resolution**: neither theme is revealed before its list. Recognition necessarily displays the
   unmarked lure as a test word before Compare; Compare identifies it and shows studied/unrelated/lure results together.
8. **PASS**: active measurements hush speech; final full flicker voice log proves the no-gap instruction finishes first.
9. **PASS**: first/latest persist through reload, device-only message visible, Reset confirmation and both branches tested.
10. **PASS**: all five standards-map rows have student actions: seven-stage prediction/model test; two perceptual matches/reveals;
    seven change finds and averages; ten recall/count trials with interference comparison; recall/recognition plus Eyewitness evidence.
11. **PASS with source correction noted**: named facts cross-checked above; Loftus experiments distinguished. No em dash in source;
    Curio Class is not shortened. Simplifications, historical samples and approximate values are labeled.

## Wave lessons
Each BUILD.md lesson checked, including the network-help-desk lessons:
- **PASS, Hint and voice**: live hints update immediately; Read uses the live hint; V.heard controls how-to repetition; no disabled-control entry instructions.
- **PASS, Focus and layout**: no load focus; station/card rebuilds move focus to an enabled controller; Edge, timed exposure and list restart retain a valid focus target.
- **PASS, Sizes**: 44px rail/header/action targets checked at all eight required sizes; small eyebrow raised to 10px. Final phone names wrap.
- **PASS, No giveaways**: no early numerical matches, lure labels or correct-option-position cues; movement, counting and miss gates exercised.
- **PASS, Honest numbers**: personal observations, counting eligibility, simplified retina and study-task differences labeled; no invented typical illusion percentage.
- **PASS, Standards**: all five map rows exercised by individual actions, as item 10 above. Spec names no family engine.
- **PASS, Motion off**: no endless animation; breathing dot stops; flicker defaults to hand flips. Full audit calm check clean.
- **PASS, Short choices**: compact change kinds all visible; Notebook rebuilt as table with sticky Go column; all six Go buttons verified even at 375px.
- **PASS, Resize mid-animation**: full audit resized after every state/input/walk action; no exceptions or permanently disabled controls.
- **PASS, Welcome timing**: Bench-first welcome tested; station-first how-to replaces generic welcome, with no late replay.
- **PASS, Unknown as unknown**: unrun Notebook says Not measured and hides comparison answers; eye output waits for prediction.
- **PASS, One look, one meaning**: orchid is observed output/selection, gray is reference/input; hollow always means counting eligibility warning, explained in text.
- **PASS, Truthful badges**: complete means a complete run, not correctness; practice/seen twice/hollow labels reflect actual state.
- **PASS, Hints change back**: new trial, rerun, scene miss, mode change and restored stage reset their live instructions.
- **PASS, No word-copy answers**: unmarked recognition lure, untitled unknown scene change, shuffled choices and context-free adjustment controls.

## Audit leads
Full audit ran once and completed within its 40-minute limit: `_scratch/illusion-lab/audit/audit.md`, **122 leads**, 129 frames.
Its frozen bundle predates the following repairs. Did not run a second audit or start a polish round.
All leads are covered below, including repeated occurrences across states/sizes:
- **Fixed** all 43px rail targets at 680/800/1000/760 and phone, phone Sound/Read targets, and the 9px eyebrow.
- **Fixed** lost focus for all six station cards, Bench Notebook/Eyewitness, Eye prediction, Change Start, Count Start,
  Words Start/second list, Why, Compare/rerun transitions. Focus now goes to a live relevant controller.
- **Fixed** the 88%-visible experiment/results region and 680px change hint clipping. Main grid now has a bounded row;
  short navigation uses two columns, stage children fit the stage, and compact change controls use two columns.
- **Fixed** disabled-control names in Shadow entry and Change entry/frozen states; also corrected analogous line/square-B entry wording.
  Last-spoken historical log entries may describe an earlier phase; the actual live hint and Read now match the current phase.
- **Fixed** unnamed recall input with explicit aria-label.
- **Fixed** every Notebook/reset-state short-choice lead (1 to 5 hidden Go buttons): replaced vertical cards with the specified table,
  sticky action column, compact header and wrapped phone labels. All six targets checked at all sizes.
- **Fixed** first-tap Bench welcome suppression and the Sound-toggle header shift using fixed button widths.
- **Intentional, BASELINE 16**: first tap directly into a station or special page speaks its own instruction, suppressing generic welcome.
  Sound off intentionally cuts narration; Read intentionally reads the live hint. No late welcome is queued.
- **Intentional** mode entry rebuilds the stage; it now retains purposeful focus. Audit reports zero header-segment modes because
  navigation is a rail; the explicit 20-state manifest covers these views.
- Motion off, resize mid-action, held-repeat controls and quick-repeat controls were clean in the full audit.
Final repair evidence: 120/120 targeted assertions in `post-audit/checks.json`, phone target/name checks, final voice logs and screenshots.

## Frames looked at
Opened all captured PNGs, including 129 full-audit frames via 22 contact sheets and relevant full-size originals.
Also inspected all station entries, Compare/Why, memory counting/recall/recognition, all Seen/all New, endpoints, real drag and keyboard,
all seven desktop sizes, 375px iframe, Motion off, grayscale, focused compact repairs, voice-walk frames and final classroom/living-room composites.
Evidence folders: `first-frames`, `functional`, `late-frames`, `phone-frames`, `phone-final-frames`, `phone-final2-frames`,
`compact-final-frames`, `compact-latest-frames`, `targeted-frames`, `endpoint-final-frames`, `voice-frames`, `voice-final-frames`,
`voice-latest-frames`, `post-audit`, `bounds`, `final-art-frames`, `audit`. Earlier failing frames are retained as provenance.

## Art made
17 generated illustrations: bench, cards, stopwatch; kitchen/street/pond/classroom/market/harbor/living-room scenes;
kettle/mailbox/boat/plant/oranges/buoy/frame overlays. Prompts and raw originals retained; all assets mark `people: false`.
Four additional redraw/edit calls removed unrelated bust/inkblot material and repaired shelf/wall placement; 21 image calls total.
Exported art: **764.17 KiB**, against the pre-build 1,150 KiB image budget. Voice **0 KiB**. Final bundle **1147.42 KiB**, below 2 MB.
Cutouts have transparency, despill and interior holes; change frames are composed exactly from one base plus localized overlays.
The classroom plant is four percent lower to meet its painted shelf, still inside the unchanged padded hit region; documented in handoff.

## Art still to paint
None. No people were needed. All planned generated assets are included; numerical/anatomical pathway diagrams remain code for accuracy.

## Engine changes wanted
None required. Shared kit, scripts and engines were left unchanged.

## Left open
Fresh sensitivity review of the disputed cultural explanation and wrongful-conviction wording before release, as the spec requests.
The named Schedar voice has no recordings in this build; browser fallback voice varies by device. Recording is outside this build's instructions.
These are classroom demonstrations, not validated individual assessments or replications of published effect sizes.
Spec contradictions and chosen interpretations are recorded in `handoff.md`; the spec itself is unchanged.
Final validation manifest: `_scratch/illusion-lab/final-validation.json`. Temporary host removed; owned Chrome/server processes closed.
