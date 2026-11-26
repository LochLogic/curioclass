# Illusion Lab: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: illusion-lab

#### Built
Built 2026-11-07 in `S:\CurioClass-codex`. Build only; no commits, deployment, shared-file edits or polish round.
The single offline deliverable is `illusion-lab.html`; edit `src.html` and bundle with `CURIO_DRAFT=1`.
Six full station state machines, Do/Compare/Why, a painted Bench, first/latest Notebook table, Eyewitness, keyboard input,
Motion off, real measurement timing, and kit narration are implemented. Metadata is beta / built.
All work is confined to `tools/illusion-lab/` and `_scratch/illusion-lab/`. Chrome used only 9990 through 9997; host 8795.
Source, notes, draft metadata, 17-line voice manifest, 20-state audit manifest, prompts, WebPs and handoff are included.
No audio was recorded. The bundler's missing-recording notices are expected; browser speech is the kit fallback.

#### Numbers check
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

#### Facts checked
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

#### Break it
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

#### Voice walk
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

#### Feel check
Best moment: Bridge joins squares that still look different into a visibly continuous gray, tying a personal setting to a physical reveal.
Later rounds change fin angle/control, true gray, retinal pattern, scene and change kind, distractor delay/category, or recall versus recognition.
Two flattest build moments were the clipped compact Bench and floating-looking change objects. Rebuilt the short-screen grid;
repainted a shelf and bare wall so the plant and frame belong in their scenes. Both final composites inspected at 1366x768.
Compared the Bench frame beside the existing Beat Lab and Snowy Mail Route bundles. Kept their standard of visual specificity,
while using an orchid-accented observation lab, painted scenes and deliberately neutral experimental stimuli.
No decorative art is added inside exact-value line, gray, retinal or memory stimuli. Graphics support the experiments' teaching.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
Opened all captured PNGs, including 129 full-audit frames via 22 contact sheets and relevant full-size originals.
Also inspected all station entries, Compare/Why, memory counting/recall/recognition, all Seen/all New, endpoints, real drag and keyboard,
all seven desktop sizes, 375px iframe, Motion off, grayscale, focused compact repairs, voice-walk frames and final classroom/living-room composites.
Evidence folders: `first-frames`, `functional`, `late-frames`, `phone-frames`, `phone-final-frames`, `phone-final2-frames`,
`compact-final-frames`, `compact-latest-frames`, `targeted-frames`, `endpoint-final-frames`, `voice-frames`, `voice-final-frames`,
`voice-latest-frames`, `post-audit`, `bounds`, `final-art-frames`, `audit`. Earlier failing frames are retained as provenance.

#### Art made
17 generated illustrations: bench, cards, stopwatch; kitchen/street/pond/classroom/market/harbor/living-room scenes;
kettle/mailbox/boat/plant/oranges/buoy/frame overlays. Prompts and raw originals retained; all assets mark `people: false`.
Four additional redraw/edit calls removed unrelated bust/inkblot material and repaired shelf/wall placement; 21 image calls total.
Exported art: **764.17 KiB**, against the pre-build 1,150 KiB image budget. Voice **0 KiB**. Final bundle **1147.42 KiB**, below 2 MB.
Cutouts have transparency, despill and interior holes; change frames are composed exactly from one base plus localized overlays.
The classroom plant is four percent lower to meet its painted shelf, still inside the unchanged padded hit region; documented in handoff.

#### Art still to paint
None. No people were needed. All planned generated assets are included; numerical/anatomical pathway diagrams remain code for accuracy.

#### Engine changes wanted
None required. Shared kit, scripts and engines were left unchanged.

#### Left open
Fresh sensitivity review of the disputed cultural explanation and wrongful-conviction wording before release, as the spec requests.
The named Schedar voice has no recordings in this build; browser fallback voice varies by device. Recording is outside this build's instructions.
These are classroom demonstrations, not validated individual assessments or replications of published effect sizes.
Spec contradictions and chosen interpretations are recorded in `handoff.md`; the spec itself is unchanged.
Final validation manifest: `_scratch/illusion-lab/final-validation.json`. Temporary host removed; owned Chrome/server processes closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: illusion-lab

#### Played
Cold Grade 12 student walk through all six stations, Compare/Why, Notebook and Eyewitness before reading builder notes or source; then checked projection and phone use through Teaching, Play and Craft.
The Bench and contextual gray reveal are strong. Kept the orchid lab identity, painted scenes, exact stimuli and unhurried experimental timings.

#### Findings fixed
- **Blocker, general, Spot the Change:** rapid manual Flip made 12 alternations in 2.4 seconds. Applied the automatic mode's minimum 720 ms cycle; the identical attack now makes 3 in about 2.3 seconds.
- **Blocker, general, change-kind check:** a wrong kind followed by another kind could save an ordinary Found. Kept retries and three misses, but corrected kinds cannot qualify as uncued finds or improve averages. Earlier ambiguous records are conservatively excluded without overwriting their numbers.
- **Should fix, general, Inside the Eye:** “changes most” conflated absolute signal reduction with neighbor contrast. Prediction and comparison now specify neighboring outputs; every incomplete state names the next enabled action and required Pattern.
- **Should fix, general, charts:** first/digit labels collided and compact charts hid final points off screen. Added numbered markers, a separate legend and real-pixel compact layouts for line, shadow, counting and word references; resize replaces only the chart, preserving control focus. Restored the wide counting chart's missing 0/50/100 percentage ticks exposed by its audit frame.
- **Should fix, general, voice:** recall, next-trial, second-list and familiarity-tag waiting steps lacked narration. Added scoped how-to lines, immediate first-tag narration and stale-speech cancellation. Included fixed Read hints in both allLines and the 57-line manifest.
- **Should fix, general, research attribution:** corrected notes' Loftus speed mean from 40.5 to 40.8 mph. Removed the unsupported attribution “They called it decay” from Peterson's explanation and qualified Keppel's near-perfect first-trial result as its stronger-learning experiment.
- **Should fix, general, result wording:** a typed unrelated word could contradict “Typed a word that was never shown: no.” The row now specifically identifies the unshown theme. Eyewitness reports an unshown inclusion without assuming how it felt.
- **Should fix, general, result/state fidelity:** failed no-gap scenes now say Not found in Notebook, rather than 0 alternations. Correct-kind selection hushes its stale instruction; Bridge off and live manual changes update hints; Trial/pressed states survive Why/Compare.
- **Should fix, general, Notebook:** audit confirmed the pinned Go column covered results. Moved each Go into its station cell, keeping navigation visible on entry without an overlapping fixed column. Why/Compare transitions now move focus to the active step when their initiating button disappears.
- **Polish, general, flattest transition:** Shadow Compare's generic completion hint skipped its best moment. It now directs Bridge, Hide the scene, then Why.
- **Polish, general, art:** edited the buoy with built-in image generation to remove attached water that also changed hue. Preserved its painted metal, light and silhouette; rekeyed with art.py. Added distinct code symbols and material shading to the flat eye-path cards.

#### Findings left
No known blocker or should fix remains among confirmed findings. Final audit resize-stress coverage is incomplete, as recorded below.

#### Break it
- Lines: tried untouched Lock, repeated tiny adjustments, endpoint mashing and rhythmic completion. Untouched/clamped entries cannot save; rhythmic entries produce arbitrary observations, with controls visible beside fin trials, never an accuracy award or best score.
- Shadow: tried untouched Lock, range endpoints and repeated tiny lightening. Gates hold. All four matches complete; A/B samples remain exactly 110 or 121 during Bridge/Hide for both trials.
- Eye: tried Middle, sweeping only the slider, and clicking all stages/patterns. A sweep alone cannot complete; all seven stages and three patterns are required. Either hypothesis leads to the same model evidence, without a guessing reward.
- Change: tried a correct spot before any alternation, fixed-corner mashing, a wrong kind, repeated kinds and three misses. Premature guesses fail; three misses yield Not found. Kind elimination is recorded as corrected, excluded from uncued averages. Completed familiar sets remain unsaved practice.
- Manual Flip: repeated rapid presses no longer accelerate the blank sequence. Motion off still defaults to manual; image and counting/list timings are retained.
- Count: completed ten no-count/empty-recall trials and ten real-timed correct-count/empty-recall trials. All ten no-count trials are hollow/excluded; all ten correct-count trials qualify. A single correct tap over 18 seconds also stays hollow (1/6 steps). No tap rhythm earns an ability score; paper/rehearsal remain outside-app limitations stated in notes.
- Words: all Seen exposes 5/5 unrelated false positives; all New exposes 0/6 studied hits. Tried empty recall, unrelated input, plural duplicates and all Picture it tags. Replaying both lists marks both seen twice and mutes their Compare cards. No blanket-response pattern earns success; neither lure is disclosed as a lure before Compare.
- Notebook: first survives new runs and reload; latest/run count update. Cancel preserves data; Yes clears the dedicated test profile's results. No unfinished run replaces a complete one.
- Why/Eyewitness: visiting earns no score. Reflection follows observed input without asserting a false feeling or an error the student never made.

#### Voice walk
Held native clicks, 120 ms presses and two-second gaps; default Sound/Motion on. Evidence: Scratch native-main, native-count, native-words-seen, native-words-new and native-change; final repair walk in native-change-repaired, each with __tool.vlog.
Main order: Line Lengths (llHow, llDone), Why; Shadow (ssHow, ssB), Compare/Bridge (ssBridge); Eye (eyeHow, eyeSlide, eyeBands); Notebook (nbHow), Eyewitness (ewHow).
Count: cbHow, cbRecall, cbNext. Words: wlHow, wlRecall, wlNext, wlTest, wlTag. Change: scHow, scKind, scNoGap. The final no-gap line played without a cut before Start enabled.
How-to counts: cbRecall 1/10, cbNext 1/9, scKind 1/7; recognition tag 1/12. Result event llDone 2/2. Five repeated Eye/Shadow visits add no how-to narration.
Read with Sound off speaks the live hint; mode switching releases Read immediately. Active measurements hush narration; the required control-entry instructions start once. Browser fallback is used because recording is prohibited.

#### Facts checked
- 1889 origin, narrower angles and practice: [Dewar 1967](https://www.appstate.edu/~steelekm/classes/psy4215/Documents/Dewar1967-muller-lyer.pdf). Feedback decrement: [Brosvic and Finizio 1995](https://pubmed.ncbi.nlm.nih.gov/7567409/).
- Cross-society findings and disputed carpentered-world cause: Segall, Campbell and Herskovits 1963, examined in [Amir and Firestone 2025](https://perception.jhu.edu/files/PDFs/25_MullerLyer/AmirFirestone_MullerLyer_2025_PsychReview.pdf). Difference is separated from causal proof.
- Identical grays, surround contrast, lighting inference and useful constancy: [Adelson 2000](https://www.cns.nyu.edu/csh/csh04/Articles/Adelson-00.pdf); 1995 credit checked against [MIT's checker-shadow publication record](https://persci.mit.edu/gallery/checkershadow). Model 200 x .55 = 110 and 220 x .55 = 121 independently recomputed and pixel-probed.
- Retina/transduction, bipolar and ganglion cells, optic nerve, thalamus and occipital cortex: [OpenStax 5.3](https://openstax.org/books/psychology-2e/pages/5-3-vision). About 92 million rods, 4.6 million cones and variability: [Curcio et al. 1990](https://pubmed.ncbi.nlm.nih.gov/2324310/); 20:1 is computed.
- Lateral inhibition and horseshoe-crab research: [Rockefeller University's Hartline history](https://www.rockefeller.edu/our-scientists/h-keffer-hartline/2487-nobel-prize/). The stated toy rule independently gives .58/.08 against .48/.18; patch interior .30 on both surrounds, edges .36/.24.
- Flicker, attention and central/marginal interest: [Rensink, O'Regan and Clark 1997](https://cim.mcgill.ca/~clark/vmrl/web-content/papers/jjclark_psych_sci_1997.pdf). Original illustrations are demonstrations, not normed scenes. 560+160 ms gives about 1.389 blanks/second; manual cap checked against [W3C SC 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html).
- Rehearsal prevention and approximate 3/18-second endpoints: [Peterson and Peterson 1959](https://psych.hanover.edu/classes/Cognition/papers/Peterson%20%26%20Peterson%201959.pdf). Their fluctuation-model discussion does not justify the former decay attribution.
- First-trial learning and proactive interference: [Keppel and Underwood 1962](https://doi.org/10.1016/S0022-5371(62)80023-1), experiment 2. Category-switch release: [Wickens, Born and Allen 1963](https://doi.org/10.1016/S0022-5371(63)80045-6).
- Ebbinghaus's 1885 publication and rapidly falling then slower curve: [Murre and Dros 2015](https://doi.org/10.1371/journal.pone.0120644); its task/measure differs from this short-term demonstration.
- Encoding/storage/retrieval: [OpenStax 8.1](https://openstax.org/books/psychology-2e/pages/8-1-how-memory-functions). Forty and 55 percent lure recall, remembered experience and reconstruction: [Roediger and McDermott 1995](https://psychnet.wustl.edu/memory/wp-content/uploads/2018/04/Roediger-McDermott-1995_JEPLMC.pdf). Original visual lists are explicitly distinguished from their spoken lists.
- 40.8/34.0 mph and, in different participants, 16/50 versus 7/50 glass reports after a week: [Loftus and Palmer 1974](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/c/571/files/2024/08/LoftusPalmer_ReconstructionAuto_JVLVB1974.pdf). Percentages recompute to 32/14; public speed estimates remain approximate.
- Sixty-nine percent of the historical 375 US DNA exonerations, 1989-2020: [Innocence Project](https://innocenceproject.org/dna-exonerations-in-the-united-states/). The card explicitly excludes an inference about all witnesses or convictions.
Independent calculations and timing totals: Scratch review-numbers.json. Both catalog standards, APA.Biological and APA.Cognition, map to the five hands-on rows exercised above.

#### Sensitivity
Next sensitivity reviewer: inspect the culture card's disputed causal framing, without treating societies as a hierarchy; inspect Eyewitness's humane wrongful-conviction language and historical denominator.
The anatomical pathway is explicitly simplified. No personal testimony or ability/body label is requested. Empty controlled scenes deliberately contain no people; all 17 assets are correctly marked people:false.

#### Flattest moment left
The quiet waits in memory presentation/counting are least varied, but their real timing is part of the experiment and was preserved.

#### Graphics
Opened all 17 assets and all seven final scene composites; inspected phone, grayscale, path cards and both gray reveals. One buoy edit via built-in imagegen, prompt retained in art/prompts.json; raw at art/raw/il-buoy.png and consumed asset art/il-buoy.webp.
Compared existing Beat Lab and Snowy Mail Route bundles without writing their folders. Kept the lab's richer painted setting and exact neutral stimuli. Bundle size: 1161.6 KiB; no missing art or people placeholders.

#### Audit
Audit not finished: ran scripts/audit_tool.py once on Chrome 9961 / host 8765 with the 2400-second limit. All eight sizes, 22 planned states, Motion off, 20 Bench-control probes and the reported repeat/quick-tap probes completed; final resize stress is unverified.
Reviewed all 139 audit frames. Of 52 leads, 18 are intentional reset-modal coverage and 16 are the spec-required skipped welcomes. The other 17 Notebook overlaps and one Why focus loss were confirmed and repaired; frame inspection also exposed the missing wide percentage ticks.
The frozen audit predates the final narrow repairs. Re-shot Notebook at all eight sizes, including the 375-pixel iframe; checked focus at 680/1366 and chart extremes at 1366/1920. Twenty-seven final targeted frames and the native repair walks had zero browser errors. No second full audit was launched.
The Windows watchdog fired at 2400 seconds but process-tree cleanup was denied. Closed its Chrome through CDP, then stopped the identified audit Python process directly. All assigned browser ports and the host port are closed.
Evidence: Scratch review-audit/audit.md, native-change-repaired, review-repair-functional, review-notebook-final and review-validation.json.

#### Left open
Fresh sensitivity judgment belongs to the next named review. Browser voices vary until the later recording stage; no clips were recorded here.
The final audit's resize-stress phase is unverified after its limit. Earlier targeted count-chart resize checks preserved layout and control focus; they do not substitute for a completed full stress phase.
Unattended choices preserve the six-station brief, timings, neutral stimuli and three-miss teaching loop; correction labels protect the existing measurements. Spec contradictions already documented in handoff remain resolved as required task content, not new topics.
Only this tool and its Scratch folder were written. No commits, shared kit edits, deployment or second full review. Execution batches use 120-second bundle, 300-second drive and 2400-second audit deadlines.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Illusion Lab: build handoff

#### Structure
`src.html` starts from the shared starter and uses kit:curio plus kit:theme-912. The tool owns the rail, responsive workbench,
six station state machines, exact canvas stimuli, original picture pairs, result charts, Why cards and Notebook.
Search for renderLines, renderShadow, renderEye, renderChange, renderCount, renderWords and renderCompare.
Curio.voice owns narration. `state.measuring` hushes speech and disables Read. No recorded audio is included.
The visual pathway and charts use code because their values and moving parts must remain exact.

#### State and timing
`illusion-lab-v1` stores only first and latest complete runs plus run counts, with try/catch. Unfinished work is discarded on a rail change.
Line and shadow movement gates count total distance moved; endpoint submissions are refused or replayed.
Count Backward uses real elapsed time and actual counting responses. Word Lists preserve the specified visual presentation timings.
Leaving the page during a timed memory run starts a fresh run, avoiding background-tab timing distortion.
All fourteen change frames are composed and loaded before Start. A scene's gray blank is computed from its base image.
Change input supports mouse location or a keyboard crosshair. Repeated completed scene sets are practice and not saved.
An actual alternation is required before a find can count. A premature correct-location guess is a miss and resumes the scene.
This closes a build-test shortcut that could otherwise save a correct find from only one picture.

#### Open questions and choices
- Sensitivity: retain the spec's open disagreement on cultural explanations, with a fresh review before any release. No society is named or ranked.
- Eyewitness: retain the historical 1989 to 2020 denominator. Do not silently substitute current exoneration totals.
- Source correction: the original Loftus and Palmer paper separates the speed estimates (experiment 1) from the later glass reports
  (experiment 2, different participants). The card now explicitly distinguishes those experiments instead of implying one continuous group.
- Contradiction: “Do-step controls never show numbers” conflicts with counting choices, trial progress, inhibition values and receptor counts.
  Retained the numeric task content required by those stations. Line and swatch values remain hidden until Compare.
- Contradiction: “lures named only in Compare” conflicts with showing the lure as an ordinary recognition-test word.
  The theme is hidden before the lists; the recognition lure is shown as an unmarked test item and identified only in Compare.
- Contradiction: the source's “720 ms cycle” is the image-plus-blank half-cycle. Full A/blank/B/blank cycle is 1,440 ms.
  Implemented 560 ms image plus 160 ms blank per alternation, approximately 1.389 blanks per second.
- Numeric discrepancy: absolute four-percent hit-box padding produces 1.68% to 8.40% frame areas before moved-position unions,
  rather than 0.8% to 6.2%. Kept the explicitly specified geometry and documented computed random-hit odds in Scratch.
- Voice instruction windows: task entry, a paused kind choice and inter-trial prompts are outside active measurements.
  Read is unavailable during active adjustment, flicker, word presentation and counting. No-gap Start waits for its instruction.
- STANDARDS takes precedence over the exact llHow, ssHow, ssB and scHow wording: entry lines now name only currently enabled controls.
  Lock instructions appear after sufficient movement; Spotted it appears in the running hint. This avoids telling a student to use a disabled control.
- Notebook uses the specified table; the cold review moved Go into the station cell after confirming the pinned column covered results. Its nbHow line now explains horizontal scrolling. Unfinished stations
  show no comparison answer. On short screens the navigation rail uses two columns so every station remains available at 44 pixels.
- The no-gap instruction has both a minimum reading window and a voice-queue guard. Muting or pressing Read cannot shorten that window.
- The brief's write boundary prevents rebundling the two bar tools. Opened their existing bundles without changing their folders.
- The brief's stop-on-report rule takes precedence over the guide's request to start a report early. The report is written after all checks.
- Art uses the user-requested image tool rather than older Gemini-specific art wording. All assets depict no people.
- The first bench and classroom candidates introduced unrelated bust/inkblot material. Both were redrawn or edited before use.
- The final classroom painting placed its narrow shelf at y 0.35. The plant is drawn four percent lower, still entirely inside
  the spec's original hit box plus its four-percent padding. The hit box itself stays unchanged. The living-room window was repainted
  as bare plaster so the moving frame hangs on a wall. These keep the object placements physically plausible.

#### Sensitivity
Cross-cultural perception research and wrongful convictions need fresh review. Check the culture card for treating the 1960s hypothesis
as a disputed explanation rather than a societal ranking. Check Eyewitness for humane wording and historical-denominator clarity.
The tool depicts an anatomical eye and teaches sensory cells. No individual is assigned a body, intelligence or personality label.
The Eyewitness closing question is conditional because not every student reports a false word. No personal account is requested.

#### Engine changes wanted
None required. Future recorded calm-professor clips would make the named voice consistent across browsers, but recording was prohibited in this build.

#### Scope
Build only. No commits, shared engine edits, publication or polish round. Validation artifacts, scripts, profiles and contact sheets live in
`_scratch/illusion-lab/`. The generated `illusion-lab.html` is the single offline deliverable; edit `src.html`, then bundle again.
The full audit ran once. Its frozen host bundle predates the repairs; `post-audit/checks.json` records 120 final targeted assertions.

#### Cold review changes, 2026-11-07
Manual Flip now shares the 720 ms minimum cycle with automatic flicker; rapid clicks cannot create fast blank flashes.
Wrong-kind retries still resume the scene and use the specified three-miss limit. They are recorded as corrections,
excluded from uncued-find averages. Earlier records with misses and no kind history are shown as earlier-method finds,
excluded conservatively without changing their stored first/latest numbers.
Eye prompts concern neighboring output contrast, not absolute input-to-output change. eyeGuide names the next enabled
action after every model change. Seven distinct code symbols and shaded pathway cards lift the diagram without adding anatomy.
Compact line, shadow, recall and word-reference charts reflow at actual pixel size rather than hiding their final points off screen.
Count first/digit dots use numbered markers and a separate legend. Shadow Compare leads directly to Bridge.
New how-to lines cover recall, the next counting trial, the second list and familiarity tags. State transitions hush stale speech.
Word recall names the unshown theme specifically; Eyewitness states what was typed without inferring how it felt.
The primary Loftus and Palmer table gives 40.8 mph, corrected in notes; the public rounded figure remains about 40 mph.
The buoy was edited with the built-in image generator, preserving its painted metal while removing attached water.
Raw prompt, original copy, rekeyed asset and final scene evidence are in this tool and its Scratch folder. No audio was recorded.
Unattended choice: preserve all six stations, original timings, exact stimuli and the three-miss learning loop. Measurement
validity labels clarify corrected observations; they add no score, topic or mode. No shared kit change is needed.
READ_HINTS contains the fixed live hints used by Read; Curio.voice receives those alongside the event/how table.
allLines and voice/lines.json now agree on 57 strings. The first familiarity-tag how-to interrupts the earlier test how-to.
The Peterson explanation now avoids attributing a decay conclusion to a paper that fitted a fluctuation model;
Keppel's near-perfect first-trial claim is qualified as the stronger-learning experiment. Sources and note links were checked anew.

Cold audit follow-up: Notebook Go buttons share each station cell, so they cannot cover first/latest/comparison text.
The failed no-gap result says Not found, rather than reporting a misleading zero-alternation speed. Corrected and legacy
no-gap results carry the same validity labels as Compare. The existing first/latest payloads remain intact.
Why and Compare restore focus to their active tab if the initiating button was removed.
Bridge off hushes and names its actual state; reveal trial and pressed toggles survive a Why/Compare return.
Live manual and Motion-off changes name Flip immediately. Completing a kind choice hushes its obsolete instruction.
Cold review audit ran once with the requested 2400-second limit. It did not finish the resize-stress phase.
Its 52 saved leads comprise 18 intentional reset-dialog occlusions, 16 spec-required skipped welcomes,
17 instances of the Notebook pinned-column defect and one Why focus-loss defect. Both confirmed defects are repaired.
Windows taskkill denied the watchdog's process-tree cleanup; the audit Chrome was closed through CDP and the identified
audit Python process was stopped directly. Host and browser ports were then verified closed. No second audit was launched.
Final native repair walks and scoring checks use a scratch bundle byte-identical to the delivered bundle; Notebook,
focus-return and percentage-axis checks use the delivered bundle. Wide counting charts now include 0/50/100 percentage ticks.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
