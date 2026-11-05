# Codex report: character-voice-booth

## Built
Built Booth, Compare and Plan as one offline HTML file, with twelve original generated paintings.
Booth captures, measures, shelves and replays up to six takes. Compare overlays takes and runs Mystery listener.
Plan supports live performance without a microphone and measured checks after microphone access succeeds.
Change one thing compares a usual take with a second take and names every dial that changed.

The source uses the kit starter, Curio.voice, Motion and tones. No family engine is specified.
All authored files are inside tools/character-voice-booth/ and its Scratch folder. No commits or polish round.
The final bundle is 521570 bytes, approximately 509.3 KB. No external asset URLs or unresolved asset tokens remain.

## Numbers check
Recomputed Sources before building in _scratch/character-voice-booth/setup.py and numbers.json.
220 to 330 Hz is 7.0195500 steps. The longest specified ghost is 8 / 1.375 + 2 = 7.8181818 seconds.
The shortest line at the fastest speed, without pauses, is 1 second. Speed shares give -45, -20, 0, +25 and +60 percent.
Pitch notches are -7, -3.5, 0, +3.5 and +7 steps. Loudness thresholds at 3 and 8 dB classify as specified.
Main contrast ratios are 6.92, 6.31, 13.44, 5.61, 5.62 and 11.31 to one, matching Look.
The six take colors range from 6.818 to 10.066 to one on #263236.

Actual Chrome fake-microphone captures measured 220.0025 and 330.0147 Hz, with a +7.0-step readout.
Known PCM also verified faster speech-time classification, a counted gap, silence rejection and short-take rejection.
70 and 700 Hz test tones are accepted; 60 and 710 Hz are rejected.
All 5000 line/dial combinations have correct duration arithmetic and pitch, speed and loudness bins.
The only pause-fit shortfalls are the 125 four-pause combinations on the four-word line, documented below.

## Feel check
Best moment: the second captured take draws above the baseline, shows +7.0 steps and faster delivery, then becomes
a real pair to replay, compare and hide for a listener. The result belongs to this student's takes.

Flattest moment 1: the first Plan layout crammed its dials into the preview panel and shrank chart labels.
Moved desktop dials under the ghost, kept phone dials together, and redrew SVGs at actual pixel dimensions.
Flattest moment 2: a refused microphone felt like a dead end. Made Go to Plan prominent and built a large painted
performance card with all four planned choices. The partner performance remains usable without recording.

Played the complete recording, comparison, guessing and Plan-check paths with synthetic microphone audio, then
completed a keyboard-only line/card/dial/performance path. No live child or adult voice was recorded.
Compared the finished frame beside Snowy Mail Route and Beat Lab in Scratch/feel-comparison.png.
The studio, microphone, lamp, painted props and measured prints give this tool its own finished setting.

## Done when
1. PASS: five real fake-microphone captures included a baseline and character takes. The 330 Hz shorter take reads
   much higher and much faster than the 220 Hz baseline. Four readouts appear on every take.
2. PASS: held Record with explicit permission rejection shows the no-mic message and Go to Plan. Perform it works.
3. PASS: five-take capture windows contain zero spoken narration entries. Read is disabled through capture.
4. PASS: Compare's table and sentence match the measurements. Mystery hides take identities and its baseline clue;
   two correct real guesses reveal Matched 2 of 2. Working guesses are cleared on Reveal.
5. PASS: +10 dB alone meets the loudness challenge. Pitch plus loudness fails and names both changed dials.
6. PASS: Clear leaves zero takes and zero capture chunks. Tested storage was empty; no audio storage is implemented.
7. PASS: take numbers and dash patterns accompany colors. Contrast calculations match the specified range.
8. PASS for focal hierarchy: newest print is largest at 680 and 1366; the shared chart dominates school-laptop
   Compare, and the ghost stays central in Plan. Compact Compare keeps its chart above the four readable rows.
9. PASS: another Play switches immediately, Delete stops playback, mode changes stop it, and count-in Stop cancels
   without shelving. Cancel-and-retry also ends both acquired microphone tracks.
10. PASS: Record, Line and all current card choices are visible without scrolling at 680, 1366 and 760 wide.
11. PASS: the five-take log has no repeated spoken how line. Audit five-held-click cases are clean. Events recur;
    empty Compare names Booth, and repeated mode taps now preserve one complete welcome without cuts.

Evidence: functional-results.json, post-results.json, keyboard-result.json, quick-*.json and closure-results.json in Scratch.

## Wave lessons
- PASS, hint and voice: state changes update the hint immediately; Read uses current content; how lines use V.heard.
- PASS, focus and layout: controls remain stable during selection and slider input; deliberate focus uses preventScroll.
- PASS, sizes: all STANDARDS dimensions were shot. Final targeted geometry reports no small controls or clipped hints.
- PASS, no giveaways: Mystery uses anonymous shuffled numbers, neutral chart color and the complete guess bank.
- PASS, honest numbers: estimates say about, speed's word assumption is on screen, and the short-line pause limit is explicit.
- PASS, standards: planning, vocal performance, revision, fair tests, comparison and listening teach the five named standards.
- PASS, Motion off: the audit found no running infinite animations; recording duration and count-in timing stay unchanged.
- PASS, short choice sets: all eight character cards, six feelings and eight open line chips stay in view. History can scroll.
- PASS, resize mid-action: the full audit found no exceptions or controls left disabled after its resize walk.
- PASS, welcome timing: first-action event lines suppress the welcome; no welcomeAfter is used.
- PASS, unknown as unknown: unavailable mic and rejected/too-short voice are explicit; no fabricated take is displayed.
- PASS, one look/one meaning: A is solid, B dashed; planned is dotted and measured solid, with labels and numbers.
- PASS, truthful badges: Take IDs never renumber; requested-versus-fitted pauses are distinguished on the short line.
- PASS, reversible hints: mode, card, line, slider, clear, delete and playback changes restore their current next action.
- PASS, no word-copy answer: listener guesses derive from the performance; take identities and baseline clue are hidden.

## Audit leads
One full audit completed in 1444 seconds, below the 40-minute limit, with 19 leads. No full rerun.
- Fixed four small Plan-tab targets with a 44 px minimum width.
- Fixed four compact Card-label box overlaps by reserving the tab area.
- Fixed the phone studio-label overlap by removing the decorative copy there.
- Fixed two unnamed empty take pickers with explicit names; they are disabled until two takes exist.
- Fixed three quick-mode welcome cuts by preserving narration when the current mode is tapped again.
- Accepted two main-hint visibility leads behind modal dialogs. Each dialog has its own instruction and trapped focus.
- Accepted three missing-welcome leads on Record, Clear and Change one thing: their own event/how line takes precedence,
  as required by STANDARDS and the kit's first-tap rule.

Nine targeted geometry cases are clean, including all affected sizes, both phone modes, empty Compare and checked Plan.
The three quick-mode retests each show one spoken welcome and no cut. All final drive batches have no console errors.
The initial extreme-state audit drag recipes returned no points. Corrected the saved recipes and independently tested
timing-jittered real drags: all four high notches and the longest slow/four-pause plan are reached correctly.

## Frames looked at
Inspected initial Booth/Plan at 680 and 1366, all three modes at every STANDARDS size, 375 px iframe views,
high/low plans, feeling and line choices, grayscale, Motion off, keyboard focus, and recording/count-in frames.
Inspected two-take and six-take shelves, Compare, Mystery Reveal, measured Plan and performance cards.
All 73 full-audit frames were inspected in thirteen contact sheets; affected frames were revisited directly.
Inspected post-frames/, last-frames/, closure-frames/ and their contact sheets, including the short-line limit.
Frame locations, inputs and PNGs are under S:/CurioClass-codex/_scratch/character-voice-booth/.

## Art made
Twelve images made with the built-in OpenAI image tool. All twelve are used. No people were generated.
Prompts and house style: tools/character-voice-booth/art/prompts.json. Raw originals and finished WebPs are retained.
Total WebP art is 318572 bytes, about 311.1 KB. Final bundle is about 509.3 KB.
No paintings were redrawn. Three cutouts were rekeyed again to clean green remnants.

## Art still to paint
None.

## Engine changes wanted
None. No shared kit, script, site template or other tool source was edited.

## Left open
- SPEC CONFLICT: the four-word line has only three internal gaps, while the spec offers four pauses for every line.
  Retained the five notches, drew three legal gaps and labeled the three-of-four fit. The owner must reconcile this
  case in the spec; no within-word or trailing ghost pause was invented.
- LAYOUT VARIATION: newest chart height is exactly twice the others. Whole cards include fixed 44 px buttons and
  full readouts, so their complete height ratio is not exactly two.
- At 375 px, full plots follow the controls and require scrolling. Primary choices and actions remain in view.
- The iframe microphone question is documented in handoff.md. A blocked preview offers Plan and a full-screen cue;
  the tool cannot grant its own iframe microphone permission, and the shared site template was not changed.
- Narration uses browser fallback. The manifest selects the kept smooth-narrator/Algieba voice and lists 71 lines;
  no narration was recorded, as instructed. Real classroom speech and paired live performance remain for cold review.
- The full audit predates its fixes; only the affected checks were repeated. No owned Chrome, host server or host.html remains.
