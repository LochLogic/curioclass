# Codex report: audience-talkback

## Built

An offline theater experiment with Watch, Swap lab and Talkback, ten original paintings, live staging switches,
two original Web Audio loops, a fair-test notebook, personal chart, criteria, verdicts, three audience cards and
temporary Class vote. Notes save locally and can be cleared. No commit or polish round.

The required acted character clips are not recorded because CODEX-BUILD.md prohibits recording audio. The browser
preview is explicitly labeled; this is a material teaching and finish limitation. Handoff describes completion.

## Numbers check

PASS: _scratch/audience-talkback/check_numbers.py independently reproduces 16 combinations, four fair tests per
base, and 32.8 / 21.3 second estimates with nine gaps and the extra pre-line-8 pause.
WCAG ratios: dark/coral 6.812, ink/paper 14.776, muted/paper 8.120, ink/panel 12.584, coral/panel 5.801,
dark/A-yellow 11.934, dark/B-sky 9.465. No spec number differed.
Sixteen full silent timeline runs finished in 32.920-33.039 seconds for A delivery timing and 21.419-21.469 for B.
The observed pre-line-8 gaps were 1600-1615 ms and 701-713 ms. These are timer checks, not recorded-clip durations.

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All manual PNGs in early-frames, targeted-frames, targeted-frames-2, functional-frames, full-watch-frames,
full-lab-frames, full-talkback-frames and last-frames, plus post-frames, audit-followup-frames, audit-followup-final-frames, final-flow-frames,
keyboard-verified.png, both bar frames, art contact
and feel comparison. The sixteen combination end frames were inspected in two contact sheets; all 43 audit frames
were inspected in four contact sheets, with lead states also checked in individual manual frames.
Full size run: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812 in a host iframe.
Only affected compact, artwork, notebook and dialog states were re-shot during fixes.

## Art made

Ten final generated images, 446.8 KiB combined. Two kneeling bears were redrawn to remove extra wheels; the
summer otter's first failed call was retried. All images were inspected and composited at useful sizes. Edge
despill was applied through art.py --rekey. Final bundle is 774.9 KiB (793,538 bytes), well below 2 MB.

## Art still to paint

None. All ten animal/prop/stage images are present and used. No people were generated.
Audio remains to make: twenty acted scene clips and twenty-two host/card narration clips.

## Engine changes wanted

None. The existing scene-audio.json supports separate A and B recordings of identical text without a kit change.

## Left open

- Acted sample first, then twenty final clips, measured button times and an audible review of every mix.
- Host knowing-guide recordings are absent; browser speech is the current narration fallback.
- Phone lab notes follow the stage; Talkback stacks the form and replay card. The long review form scrolls in short landscape boxes.
- Final acted delivery and piano/plucked timbres still need a headphone listening review.
- Teacher counters and later long-form work may require scrolling; these are documented layout limits.
- Audit predates the focused repairs. Cold review should use the current source and corrected audit states.

All started Chrome instances and host servers were closed. No tool host.html remains. No shared file was changed.
