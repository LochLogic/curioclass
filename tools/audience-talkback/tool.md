# Audience Talkback: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: audience-talkback

#### Built

An offline theater experiment with Watch, Swap lab and Talkback, ten original paintings, live staging switches,
two original Web Audio loops, a fair-test notebook, personal chart, criteria, verdicts, three audience cards and
temporary Class vote. Notes save locally and can be cleared. No commit or polish round.

The required acted character clips are not recorded because CODEX-BUILD.md prohibits recording audio. The browser
preview is explicitly labeled; this is a material teaching and finish limitation. Handoff describes completion.

#### Numbers check

PASS: _scratch/audience-talkback/check_numbers.py independently reproduces 16 combinations, four fair tests per
base, and 32.8 / 21.3 second estimates with nine gaps and the extra pre-line-8 pause.
WCAG ratios: dark/coral 6.812, ink/paper 14.776, muted/paper 8.120, ink/panel 12.584, coral/panel 5.801,
dark/A-yellow 11.934, dark/B-sky 9.465. No spec number differed.
Sixteen full silent timeline runs finished in 32.920-33.039 seconds for A delivery timing and 21.419-21.469 for B.
The observed pre-line-8 gaps were 1600-1615 ms and 701-713 ms. These are timer checks, not recorded-clip durations.

#### Feel check

Best moment: the otter looks up and the bear kneels at the turn in line 8; a live lighting swap reframes
the same ending, and the chart later shows the student's own comparison rather than an official favorite.
Flattest: the compact stage was initially tiny and its notebook hid Show my results. Moving captions to the side
during short landscape playback, simplifying compact headings and collapsing the notebook gave the art more room
and kept the last rating plus results in view. The other flat moment is the browser acting preview. Rate/volume
changes cannot supply the specified acted performances. That remains open under the explicit no-recording rule.
Watched both full versions, chose feelings, tested the mixer, rated experiments, inspected the chart and completed
criteria/verdicts/cards. The entire scene and feelings path also ran end to end in whole-watch.json.
Compared with Beat Lab in feel-comparison.png and opened both bar tools. The painted theater has comparable visual
care and stronger scene detail; authored acting still needs to match that finish.

#### Done when

1. PASS: stage and four lab switches are together at 1366x768, 680x425 and 375x812. Full mode frames and layout JSON.
2. FAIL for final acted audio: visual state changed within 10 ms and Voices immediately restarted the current line
   in live-switches.json, with the scene still playing. Browser speech cannot guarantee the specified bank delivery.
3. FAIL for the full audio requirement: all sixteen silent mixes reached ten starts and ten ends, with expected
   gaps and no runtime errors. Final clip overlap/gap testing remains impossible without the twenty recordings.
4. PASS: multiple-change rows are flagged and excluded. Real complete mixes produced these rows; chart fixture
   independently confirmed exclusion while retaining their editable ratings.
5. PASS: chart includes only rated one-element trials, largest first, labels on every bar, with repeated trials
   averaged on an explained 0 to 2 scale. No official correct response is supplied.
6. PASS: scene start hushes the host, Read is held during playback, and live-switches.json logged no host speech
   during the scene. Sound toggles preserve the scene's running state.
7. PASS: three selected criteria, six A/B ratings and both sentences survived reload in storage.json.
8. PASS: five held-click plays at a two-second pace logged one welcome/how start and five heard/silent returns.

#### Wave lessons

- Hint and voice: PASS with the audio limitation above. Immediate hints, Curio.voice scope/valid checks, Read,
  action-first scene starts and heard-line suppression verified in held-click logs.
- Focus and layout: PASS for stable mixer/criteria/rating nodes, explicit clear-dialog return and native keyboard
  traversal. Audit disposition follows below.
- Sizes: PASS for the main stage/mixer/transport at all eight sizes. Phone lab notes follow the stage; long Talkback forms scroll.
- No giveaways: PASS. Personal feelings and criteria have no correct-answer badges or hidden answer ordering.
- Honest numbers: PASS. Version times say About and the preview warning explains estimates. Chart explains scoring.
- Standards: PASS for the implemented response process. A solo learner chooses criteria, evaluates both versions,
  ties a verdict to personal experience and hears other audience perspectives. Authored vocal evidence remains open.
- Motion off: PASS. No running infinite animation; scene timing is retained. motion-off.json and frame inspected.
- Short choices: PASS in the inspected Watch feeling and six-criterion banks. Notebook history and the long review
  form are secondary scrollable work; the current compact notebook row and results stay in view.
- Resize mid-animation: PASS. Keyboard resize preserved a running line through 1366, 760 and back without errors.
- Welcome after first tap: PASS. Play skips a stale welcome; five-play logging confirms no late welcome.
- Unknown shown as unknown: PASS / not applicable to hidden evidence. Unchosen feelings and no rated tests are explicit.
- One look, one meaning: PASS. A/B letters and weather symbols accompany color; selectors and chart bars have labels.
- Badge truth: PASS. Watched requires all ten completed lines; quick playback creates no notebook row.
- Hint changes back: PASS. Mode changes and stopping playback immediately update the next action.
- No answer by word copying: PASS. Ratings, chosen criteria and personal reasoning cannot be solved by matching text.

#### Audit leads

The full audit completed once within 40 minutes: 46 leads, no runtime or resize errors, and all eight initial
sizes clean. Every finding is answered in Scratch/audit-responses.md (43 state/walk entries plus three expected
vote-control shifts). Disposition of repeated classes:

- Fixed both field-name leads with explicit aria-labelledby links to the visible starter labels.
- Fixed compact Replay/Hear access by placing the controls before the stage thumbnail; checked 680, 800 and 1000.
- Kept the later verdict textareas as a scrolling form; the six short criterion choices remain visible.
- Kept phone lab notes after the stage and stacked the Talkback form/replay card. Scrolled checks show ratings, results,
  both verdicts and replay controls accessible. Optional teacher counters also remain a scrolling extra.
- Talkback's visible #talk-hint mirrors the hidden #hint; Read uses the same current text. During compact playback,
  subtitles intentionally occupy the hint slot while switches and Stop remain visible.
- Twelve skipped Play/tick welcomes are required: the actor scene makes them stale and host speech must stay silent.
- Reset switches is idempotent at the base; real flips then Reset returned AAAA. Native vote clicks and Reset
  produced 1/0, 1/1, 2/1, 0/0. Revealing cards intentionally moves the three teacher controls below them.
Additional focused repairs: high-contrast chart words, card-hide speech cancellation, modal welcome suppression,
saved-criteria hints, reverse Tab, and a base reset on Lab entry. Watch B then Go to lab starts AAAA; Lights gives
ABAA, a fair first test. All affected checks passed without console errors. The full audit was not repeated.
The subset phone-state label was corrected to 375x812 for future audits; additional phone work was checked directly.

#### Frames looked at

All manual PNGs in early-frames, targeted-frames, targeted-frames-2, functional-frames, full-watch-frames,
full-lab-frames, full-talkback-frames and last-frames, plus post-frames, audit-followup-frames, audit-followup-final-frames, final-flow-frames,
keyboard-verified.png, both bar frames, art contact
and feel comparison. The sixteen combination end frames were inspected in two contact sheets; all 43 audit frames
were inspected in four contact sheets, with lead states also checked in individual manual frames.
Full size run: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812 in a host iframe.
Only affected compact, artwork, notebook and dialog states were re-shot during fixes.

#### Art made

Ten final generated images, 446.8 KiB combined. Two kneeling bears were redrawn to remove extra wheels; the
summer otter's first failed call was retried. All images were inspected and composited at useful sizes. Edge
despill was applied through art.py --rekey. Final bundle is 774.9 KiB (793,538 bytes), well below 2 MB.

#### Art still to paint

None. All ten animal/prop/stage images are present and used. No people were generated.
Audio remains to make: twenty acted scene clips and twenty-two host/card narration clips.

#### Engine changes wanted

None. The existing scene-audio.json supports separate A and B recordings of identical text without a kit change.

#### Left open

- Acted sample first, then twenty final clips, measured button times and an audible review of every mix.
- Host knowing-guide recordings are absent; browser speech is the current narration fallback.
- Phone lab notes follow the stage; Talkback stacks the form and replay card. The long review form scrolls in short landscape boxes.
- Final acted delivery and piano/plucked timbres still need a headphone listening review.
- Teacher counters and later long-form work may require scrolling; these are documented layout limits.
- Audit predates the focused repairs. Cold review should use the current source and corrected audit states.

All started Chrome instances and host servers were closed. No tool host.html remains. No shared file was changed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: audience-talkback

#### Played

Cold grade-4 exploration of all three modes preceded the builder's report, handoff and source. Then completed the repaired main path with Sound on and checked the projected-teacher controls. The painted theater and the bear's change to concern at line 8 are strong.

#### Findings fixed

- **blocker/general, src.html playback:** immediate speech errors completed lines in milliseconds. Speech/clip failures now preserve the remaining caption time; forced failures cannot rush the watched check.
- **blocker/general, notebook:** five base lines followed by a last-instant Lights flip and Stop produced a fair trial without observing the change. Recipe revisions and whole-line observation now keep that row out of results.
- **blocker/general, notebook:** replaced an arbitrary-five-lines predicate with the first five setup lines. Short-line hopping plus the ending cannot earn a trial.
- **should fix/general, storage:** null legacy rows aborted loading. Valid work now survives; version-1 ratings remain editable but lack verified observation and cannot contaminate new results.
- **should fix/general, hints:** base replays no longer assume a swap. Unobserved trials explicitly say to tap Play again; incomplete Watch runs retain the appropriate starting instruction.
- **should fix/general, Watch:** unreliable 33/21-second browser labels now say Timing varies. Complete future recordings calculate measured totals including pauses.
- **should fix/general, phone:** moved the hint above the stage. Hint, full-size stage, four switches, Play/Stop and ten ticks fit at 375x812, including after resizing during playback.
- **should fix/general, Clear:** clearing work also restores Base A and AAAA.
- **polish/general, results:** added a finding drawn from the student's ratings, including ties and no change. Zero ratings draw no colored bar. Four bars and their labels fit at 680x425.
- **polish/general, art:** redrew the weakest prop, the bicycle, with a clearer slack chain and damaged wheel while retaining the painted style.

#### Findings left

**blocker/general:** twenty acted character clips and twenty-five host/Read/card recordings are absent. The required [CODEX-BUILD.md](../../docs/agents/CODEX-BUILD.md) says, "Do not download anything or record audio." This review obeyed that rule. The tool remains a labeled browser preview; final authored acting, bank identities, measured clip lengths and audible mix quality are unverified. The full audio portions of Done when 2 and 3 remain open.

#### Break it

- Rapid Play/Stop rhythm and jump-to-10: no notebook row. Five short lines plus the ending: no row.
- Late switch then Stop, followed by A lot: editable unobserved row, no chart bar. A normal single swap and a genuinely observed live swap produce fair rows and correct bars.
- Two changes then undo one: both remain in the trial and are excluded. Base replay: excluded, with an appropriate instruction.
- Zero and repeated ratings: zero-length bar and correct 1.5 average. The chart states its 0/1/2 mapping; opinions have no answer key or mastery badge.
- Fourth criterion rejected. Six chosen A/B ratings and both verdicts survive a reload. Legacy notes survive safely; denied storage shows saving unavailable.
- Held teacher-counter clicks after scrolling: 1/0, 1/1, 2/1, then Reset to 0/0. This is an explicitly manual teacher counter, not a student score.

#### Voice walk

Sound on, 120 ms presses, 2-second tap pace: stage, A, B, feelings, Go to lab, Lights, Play through five setup lines, Stop, rating, results, Talkback, three criteria/six ratings, verdicts, audience cards. Both full Watch versions completed.
Line starts in order: welcomeWatch, watchNext, feelHow, welcomeLab, rateHow, welcomeTalkback, verdictHow. A full audience run then starts audienceAR, audienceLM, audienceST and talkbackDone in order, ending with an empty queue.

| Line | Kind | Expected starts | Observed |
|---|---|---|---|
| welcomeWatch | how/welcome | 1 | 1 |
| welcomeLab | how/welcome | 1 per page | 1, then 5 silent heard returns |
| rateHow | how | 1 | 1 |
| welcomeTalkback, verdictHow | how | 1 each | 1 each |
| audienceAR/LM/ST, talkbackDone | event | 1 each per full reveal | 1 each |
| Read | forced read | 2 in side walk | 2, including Sound off |

Read/hide/mode cancellation drops stale speech; no host line starts inside actor playback. Some instructions are cut when the student's next action makes them stale, as the spec requires. The new stopped-trial instruction was separately heard while Play was enabled. Logs are in ../../_scratch/audience-talkback/voice-review/ and audience-review/.

#### Facts checked

- Personal experience, differing responses, criteria and technical elements: [National Core Arts Standards, Theatre](https://www.nationalartsstandards.org/content/theatre), Re8.1.3-5.a and Re9.1.4-5.a/b. Notes identify these strands rather than implying every substandard.
- Design choices support storytelling: [Educational Theatre Association, Production & Design Elements: Where to Begin](https://schooltheatre.org/production-design-elements-where-to-begin/). No universal blue-equals-sad rule is taught.
- Controlled-variable comparisons: [NGSS Appendix F, Practice 3, grades 3-5](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf).
- Independent enumeration: 16 recipes, four single swaps per base, eight directed fair comparisons. Nine gaps plus the pre-line-8 pause total 4.8 s for A and 2.3 s for B; pre-recording estimates are 32.8/21.3 s. See ../../_scratch/audience-talkback/review-math.json.
- Contrast recomputed using [W3C WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html): coral/paper 6.812:1, ink/paper 14.776, muted/paper 8.120, ink/panel 12.584, coral/panel 5.801, dark/A 11.934, dark/B 9.465; result ticket 9.173.
- The ten-line scene, recipes, music and audience cards are original Curio Class content from the spec. The same dialogue is used in both deliveries. The knee injury is fiction, not medical guidance.

#### Sensitivity

No represented culture, religion, Native tradition or hard history; all actors are fictional animals. A reviewer should check family-experience prompts without assuming every student has a grandmother or allowance. The three cards describe individual fictional experiences.

#### Flattest moment left

The browser acting preview remains the flattest moment. Authored performances are needed for convincing vocal evidence. The formerly bare chart now ends with the student's own finding, without rewarding a preferred opinion.

#### Graphics

All ten images checked in contact sheets and stage frames; no missing listed art or people assets. Kept the theater, palette, poses and quiet motion. The bike redraw used built-in image generation; final asset is [art/bike.webp](art/bike.webp), with its prompt and provenance in [art/prompts.json](art/prompts.json). Generated alpha is preserved. Colored RGB outside alpha was invisible in the real stage, so it was not a visible keying defect.
Art totals 461.2 KiB; final self-contained bundle is 817,892 bytes, about 799 KiB. Compared the finish with the saved Beat Lab reference frame.

#### Audit

Completed the single audit within its 40-minute limit: 62 leads, 51 PNGs inspected. All eight initial sizes were clean. No runtime, focus, repeat, Motion-off or resize failures.
Phone hint placement and its inaccurate notebook keep fixture were fixed afterward. Targeted 375/680/1366 frames, a live 375-to-680-to-375 resize, scrolled notebook access, reset and held vote clicks passed. The compact feelings screen also retains every choice and tick.
Remaining leads concern intentional long-form scrolling, the visible Talkback hint's hidden mirror, required welcome suppression during actors/dialogs, idempotent resets and teacher-counter movement. Every lead has a disposition in [review-audit-responses.md](../../_scratch/audience-talkback/review-audit-responses.md).
The audit was not repeated after the phone repair. Final checks and hashes are in [review-validation.json](../../_scratch/audience-talkback/review-validation.json). Test-host favicon 404s were distinguished from tool errors.

#### Left open

Release remains blocked by the missing authored audio described above. Retained the spec's sample-first recording route without asking unattended questions. No new topic, kit change or git commit. Writes stayed in the tool and its Scratch folder; all owned Chrome/host ports are closed and no host.html remains.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Audience Talkback build handoff

#### Cold review changes (2026-11-05)

The review keeps the theater, palette and all ten painted assets. The bicycle was redrawn with a more legible
slack chain and a buckled front wheel. Its generated alpha is preserved by setting cutout false with transparent true
in prompts.json, so art.py --rekey only resizes/encodes it.

Notebook storage is now version 2. Sessions track completed first-five setup lines, a recipe revision and which
changed elements were observed for a complete uninterrupted line. A last-instant switch remains an editable note
but is excluded from results. Multiple-change and base trials remain excluded. Version-1 notes and ratings survive,
but lack verified evidence and do not enter the chart. A mixed test cannot become fair by resetting a switch.
The results ticket summarizes the student's own highest average, including ties and zero change; it awards no score.
Zero ratings draw zero-length bars. Null saved notebook entries are filtered without losing the other saved work.
Clear my notes also restores Base A and AAAA. New no-observation/base hints are in the voice manifest.

Browser preview buttons now say Timing varies. If all twenty recorded clips are supplied later, the existing
metadata automatically sets each measured duration, including the nine gaps and the line-8 pause.
Immediate browser-speech or clip playback errors now use caption timing for the remaining line instead of
counting a failed line complete immediately. Generation guards also cover this fallback. The on-screen status
names speech unavailability. A failed speech backend cannot fast-forward the scene into a watched marker.
The original no-recording restriction still applies to this review. The twenty acted clips and host recordings
remain a release blocker; none was generated or recorded here. Do not represent this as final acted audio.
The completed review audit found 62 leads, with no runtime/focus/repeat/resize failures. The final layout repair moves
the phone hint above the stage, retaining stage/mixer/Play in the viewport. Caption spacing is tightened without
reducing the art. On wider screens the hint returns to the panel before the caption is placed, so crossing the
600-pixel breakpoint while playing cannot insert a caption relative to a node in another parent.
The phone notebook remains below the stage per spec. Its audit keep regions now describe the primary controls;
the long Talkback form and optional teacher counters deliberately scroll. Full dispositions are in
_scratch/audience-talkback/review-audit-responses.md. The single audit predates this phone repair; targeted frames
and a live resize check verify it afterward. The full audit was not repeated.

The sections below preserve the builder's architecture notes; this dated section supersedes their old duration,
five-arbitrary-lines and recording-count descriptions. Review evidence is in _scratch/audience-talkback/.

#### Builder architecture

src.html starts from the kit starter. It contains the responsive theater, Watch, mixer/notebook, Talkback form,
and dialogs, followed by content, guarded storage, scene playback, music scheduling, rendering and event wiring.
It uses kit/curio.css and kit/curio.js. No family engine is specified. Nothing shared was changed.
scene-audio.json is loaded by src.html and currently contains empty A and B recording arrays.
The standard bundler produces the self-contained audience-talkback.html from art tokens, JSON and kit tokens.

window.__tool exposes state, actions, V.log as vlog, scene playback and switch timing logs, fairResults, and the
music clock. Timers carry a generation token, so an old line cannot advance after a stop, jump or delivery switch.
Voices restart the current line immediately, including during a gap. Other switches do not touch the timeline.
Both original Web Audio loops use one clock, at 72 and 112 beats per minute, with a 150 ms bus crossfade.

Notebook trials collect the union of all elements that differed from their captured Base during that play.
Base cannot change while playing. A row requires five fully completed lines and reaching the ending or stopping
after line 5. This prevents a line-10 jump or quick tap-through from creating an experiment. Multiple changes and
base replays stay in the notebook and retain ratings but are excluded from the chart. Repeated ratings are averaged
per element, with the 0 to 2 mapping written on the chart. Ratings are opinions, never checked against an answer key.

The four mixer nodes and all criteria/rating nodes stay stable under the pointer. Notebook nodes are rebuilt only
when adding or clearing rows. Ratings themselves update their existing buttons. The compact notebook shows only
its latest row; the complete list remains saved. At short landscape sizes, captions occupy the panel's hint area
during playback, leaving more room for the painted stage. The caption moves on resize; the stage moves into the
thumbnail mount on entering Talkback. Entering Swap lab resets its switches to the selected Base. This prevents
finishing Watch B from leaving four differences against Base A before the student's first one-switch trial.
Lab Tab boundaries route mixer and transport, notebook, then line ticks. Focus calls use preventScroll.

#### Open question decided

The spec leans toward hearing an acted sample before making all twenty clips. Keep the sample-first route.
The four delivery styles and speaker voices are recorded in voice/lines.json under scene_deliveries.
The build brief explicitly says not to record audio. No sample or full audio set was recorded during this Build.
The current browser speech preview is labeled on screen, with estimated version times. This is a material limit:
browser rate/volume changes do not reproduce the requested acted shaky, laughing, gentle and surprised deliveries.
Autonoe and Gacrux are the intended final voices; the browser cannot select these bank identities.

#### Audio completion route

After a future task authorizes recording, make a sample of Kit and Holloway in both styles before the full set.
The ten spoken texts are in voice/lines.json under scene_lines; poses and stage directions remain on screen.
Generate twenty distinct clips with the supplied two voices and four acted styles. The ordinary voice bundler keys
clips by text, so it cannot distinguish the same text in A and B. Put each delivery in scene-audio.json as an object
with src (an inline audio data URI) and duration (seconds), in A and B arrays indexed 0 through 9.
The existing player uses those clips, onended and error guards, with the specified gaps and pre-line-8 pauses.
Measure the sum of all ten actual clips plus nine gaps and the extra pause. Replace the estimate labels on both
Watch buttons. Test all sixteen mixes audibly and confirm no overlap or truncation. Do not silently call these
browser previews the recorded acting comparison. The host uses Curio.voice with knowing-guide / Sadaltager.

#### Art and local choices

- Ten images were made with the imagegen tool, as requested. All actors are animals; no people were generated.
- A retry made kit-b-down after its first image call returned no saved output.
- The two kneeling bears were edited to remove extra bicycle wheels. The bike is a separate composited asset.
- All cutouts use the specified flat magenta key, then the free art.py --rekey pass, with edge despill.
- Art prompts include provenance and redraw notes. Source images remain in art/raw. No external image was downloaded.
- The spec's local-FLUX suggestion yields to the user's explicit request to use the available image tool.
- The source numbers and supplied contrast ratios recomputed correctly. Notebook and chart arithmetic is tested.
- The two quality-bar tools were bundled into Scratch using the original bundler's function and copied inputs.
  Their source folders were not written. Paint Mixer lacked handoff/refine files; Art Style Match's source and
  handoff and Near and Far's handoff supplied additional built-neighbor examples. Missing refine files are absent.
- The user says to stop when codex-report.md is written. Progress therefore lives in Scratch/report-progress.md;
  the final report is written only after the checks, instead of the generic brief's early-report suggestion.

#### Storage and privacy

Only feelings, watched markers, notebook rows, selected criteria, ratings and verdicts are saved under
audience-talkback. Parsed values are bounded and validated, and user text enters the page through textContent/value.
The display states that notes never leave the device. Failed storage remains usable and reports saving unavailable.
Clear my notes clears all work after a native dialog, leaves the kit's shared Motion preference, and returns to Watch.
Class vote is temporary and independent of any student's verdict.

#### Engine changes wanted

None. A future general purpose dialogue-clip bundler could support two deliveries of the same text, but no shared
change is needed to finish this tool: its loaded scene-audio.json already supports separate inline recordings.

#### Review focus

See codex-report.md for actual check results, audit lead dispositions and any limits. The principal content gap is
the unrecorded acting. The cold review should also judge the emotion distinction of the final music and voices,
the usefulness of live swapping, compact notebook access and whether criteria judgments transfer to the verdict.
This was Build only. No polish round or git commit was made.

#### Build audit closure

The single full audit completed within its 40-minute limit with 46 leads. All eight initial sizes, Motion off,
mid-action resizing, keyboard focus, five held-click repetitions and quick repeats had no runtime failures.
Every lead is answered in _scratch/audience-talkback/audit-responses.md. The 43 state/walk entries and three
expected vote-control shifts are covered individually. Phone lab notes follow the stage; Talkback stacks its form
and replay card. Long verdict forms and optional teacher counters remain scrollable. Talkback uses #talk-hint as its visible
hint, mirroring the hidden common #hint that Read uses. Compact playback uses the hint area for subtitles.

Focused repairs explicitly link each verdict field to its visible label, put compact Replay/Hear controls before
the thumbnail, improve chart label contrast, cancel speech when cards hide, suppress welcomes behind dialogs,
and make saved-criteria hints state-aware. Native vote clicks and reset, a four-change compact notebook, reverse
Tab, Sound changes during a scene, scrolled phone work and Watch B to fair Lab entry were checked separately.
The full audit was not repeated after these changes. The subset phone-state label is corrected to 375x812 for
the cold review. All manual frames and four audit contact sheets were inspected. All started Chrome instances
and host servers were closed, and the generated tool host.html was removed.

#### Sensitivity

Original animal fiction with no cultural or religious tradition represented. The personal-life prompt must not imply that every student has a grandmother, an allowance or the same family arrangements. The audience cards are three fictional individual experiences, not claims about a whole group. No body or medical instruction is taught by the mention of a knee.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
