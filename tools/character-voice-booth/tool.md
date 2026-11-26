# Character Voice Booth: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: character-voice-booth

#### Built
Built Booth, Compare and Plan as one offline HTML file, with twelve original generated paintings.
Booth captures, measures, shelves and replays up to six takes. Compare overlays takes and runs Mystery listener.
Plan supports live performance without a microphone and measured checks after microphone access succeeds.
Change one thing compares a usual take with a second take and names every dial that changed.

The source uses the kit starter, Curio.voice, Motion and tones. No family engine is specified.
All authored files are inside tools/character-voice-booth/ and its Scratch folder. No commits or polish round.
The final bundle is 521570 bytes, approximately 509.3 KB. No external asset URLs or unresolved asset tokens remain.

#### Numbers check
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

#### Feel check
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

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
Inspected initial Booth/Plan at 680 and 1366, all three modes at every STANDARDS size, 375 px iframe views,
high/low plans, feeling and line choices, grayscale, Motion off, keyboard focus, and recording/count-in frames.
Inspected two-take and six-take shelves, Compare, Mystery Reveal, measured Plan and performance cards.
All 73 full-audit frames were inspected in thirteen contact sheets; affected frames were revisited directly.
Inspected post-frames/, last-frames/, closure-frames/ and their contact sheets, including the short-line limit.
Frame locations, inputs and PNGs are under S:/CurioClass-codex/_scratch/character-voice-booth/.

#### Art made
Twelve images made with the built-in OpenAI image tool. All twelve are used. No people were generated.
Prompts and house style: tools/character-voice-booth/art/prompts.json. Raw originals and finished WebPs are retained.
Total WebP art is 318572 bytes, about 311.1 KB. Final bundle is about 509.3 KB.
No paintings were redrawn. Three cutouts were rekeyed again to clean green remnants.

#### Art still to paint
None.

#### Engine changes wanted
None. No shared kit, script, site template or other tool source was edited.

#### Left open
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

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: character-voice-booth

#### Played
Grade 4 solo and projector paths: cold Booth, no-mic, Plan and Perform before builder notes/source.
Then synthetic MediaStream captures, checked Plan, Compare, Mystery guesses/Reveal, interruption, cancellation and Clear.
The booth and painted props are strong. The original tick-like ghost and small Reveal payoff were the flat spots.
Keyboard-only line/card/four-dial/Perform and Space playback passed; grayscale and Motion off were inspected.

#### Findings fixed
- Blocker, general, Plan: grading used the student's baseline speed while the ghost used 2.5 words/s. Both now use 2.5.
- Should fix, general, baseline: a character recorded first was falsely called the usual voice. Chart and speech name the fallback baseline.
- Should fix, general, charts: segmented strokes broke prints into ticks. Continuous paths retain loudness widths and correct dash phase.
- Should fix, general, targets: range inputs were 23/28 px high. All are now 44 px, with compact controls still visible.
- Should fix, general, hints: denied-mic/card selection, completed Reveal and family switches now retain fitting instructions and drop stale speech.
- Should fix, general, keyboard: held R ignores repeat events rather than immediately stopping its own recording.
- Should fix, general, Plan: a planned pitch beyond the chart's measurable range now has an explicit edge warning.
- Should fix, general, graphics: tiny, mixed system emoji became six consistent, shaded SVG feeling expressions.
- Should fix, general, Reveal: six results were clipped at 680x425. The recap now scrolls by keyboard, with total and return action visible.
- Should fix, general, playback: Compare/Mystery animated a hidden Booth strip. The active chart now gets its playhead or Motion-off outline.
- Should fix, general, voice: a welcome could refer to controls behind the line dialog. A once-only dialog instruction speaks there; welcome waits for close.
- Should fix, general, Perform: the listener could see the answer prop. Visible and spoken instructions now tell the listener to look away.
- Polish, general, payoff: Mystery's earned total is prominent on the main stage, including compact layouts; revealed badges/hints are truthful.
- Polish, general, weakest painting: repainted the idle lamp with dark glass, retaining its detailed red case and warm studio lighting.

#### Findings left
- Should fix, spec: four internal pauses cannot fit between four words. The existing three-of-four warning stays; see Left open.
- Polish, layout: 375 px keeps actions first and places full plots below the fold. Readable history remains scrollable.

#### Flattest moment left
Plan's usual ghost is deliberately a level line. It needs a live performance or measured take to become interesting.

#### Graphics
All 12 paintings inspected, including large performance props; one idle-lamp redraw and six code-face redraws.
The imagegen edit used the existing lamp as reference; final prompt is in art/prompts.json and raw output in art/raw/lamp-off.png.
All specified art is present and used. No people assets, missing paintings or stereotypes found.
Art: 310.6 KiB. Final bundle: 512.5 KiB, 524849 bytes. Snowy Mail Route and Beat Lab were viewed as finish bars.

#### Audit
One full audit completed in 1588.41 seconds, below 40 minutes: _scratch/character-voice-booth/review-audit/audit.md.
All 85 audit frames were inspected. Default sizes, repeat taps, rapid taps, Motion off and resize stress were clean.
Its 12 mechanical leads were reviewed: two expected modal-hint warnings; three history-scroll warnings;
three phone-plot visibility warnings; three correct first-tap own-line welcome skips; one drawing-animation keep warning.
The shelf recipe now waits 800 ms, beyond the specified 600 ms draw. Settled shelf frames confirm the newest print is visible.
The frames exposed the clipped Reveal recap and dialog narration issue; those and the hidden playback feedback were fixed.
Only affected states were re-shot afterward: recap top/bottom, phone recap, active-chart playback, modal speech and Perform instructions.
Focused drive batches had zero browser console errors. The full audit was not rerun after those scoped fixes.

Five-take narration counts, from review-five-take-voice.json:

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| First-take character instruction | how | 1 | 1 |
| Tap Compare | how | 1 | 1 |
| Baseline result | event | 1 | 1 |
| This take is | event | 4 | 4 |

Pitch/speed result parts each spoke four times. One stale comparison tail was dropped when a newer take arrived.
The line dialog spoke its own instruction, then the welcome after close. All 74 fixed lines match the final voice manifest.
Actual AudioWorklet capture of synthetic 220/330 Hz streams read +7.0 steps, faster delivery and +9.9 dB.
Capture windows had zero spoken narration entries; mic tracks ended; Play switching, mode interruption and count-in cancellation passed.
A deliberately fast baseline still yielded four correct usual-plan matches. Explicit permission denial retained Go to Plan after a card change.
Loudness-only +10 dB passed the fair test; pitch plus loudness failed and named both. Mystery matched 3 of 3 and cleared guesses.
The seventh take preserved the baseline; Clear left no take buffers or chunks. Audio has no authored localStorage path.
Recomputed 7.01955 steps, 7.81818 s longest ghost, 1 s shortest ghost, five speed ratios and all six stated contrast pairs.
Wave lessons checked: current hints/Read, stable focus, visible choices/targets, hidden answers, honest bins, all five theatre standards,
Motion off, resize, truthful badges, reversible hints and no word-copy answer. Notes retain the three required opening sections.

#### Left open
The spec requests four between-word pauses on the four-word line. Kept its explicit three-gap limit; changing the line or notch needs a spec decision.
Narration uses browser fallback; recordings remain absent under the brief's no-recording rule. No live classroom/human-voice trial was run.
Embedded microphone permission is controlled by the host page. The denied-mic Plan path works; no shared host template was changed.
No engine changes, git commits, owned Chrome/server processes or tools-folder host.html remain. One review pass only.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Character Voice Booth build handoff

#### Structure
src.html starts from the kit starter and uses kit:curio CSS, Curio.voice, tones and Motion. There is no family engine. The single-file bundle is character-voice-booth.html. Build with CURIO_DRAFT=1. Twelve paintings are listed in art/prompts.json; originals are in art/raw and final WebP files are bundled through art tokens.

The script has content and narration tables, audio analysis, ghost generation, SVG charts, three mode renderers, capture and playback, then stable input handlers. window.__tool exposes the real state, analyzer and renderers for inspection. No test data is shipped. Scratch contains test-only PCM synthesis and Chrome fake-microphone checks.

#### Tricky parts
- AudioWorklet captures mono Float32 chunks with microphone processing disabled. The embedded module is a data URL because Chrome rejects blob module loading under file URLs. The track is stopped after every take and cancellation. No MediaRecorder, network upload or persistence is used.
- Capture hushes narration before permission and disables Read through count-in, capture and analysis. Request tokens discard late permissions and canceled analysis. Count-in timing stays unchanged with Motion off.
- Analysis uses original 2048-sample windows at 10 ms hops. Samples within each frame are decimated to about 8 kHz for normalized autocorrelation over 70-700 Hz. A voiced frame requires above -45 dBFS and clarity at least 0.8. Five-frame median smoothing preserves unvoiced breaks. Speed assumes every word in the chosen line was spoken.
- Baseline is the latest My usual voice take, else the first remaining take. Deleting a baseline recalculates every readout. A seventh take preserves the baseline and drops the oldest other buffer. IDs never renumber, including after Clear.
- Plan uses the specified fixed usual speed of 2.5 words/s. A checked take retains a numeric snapshot of the reference used when recording started, so a new usual-voice take cannot move its own goalposts. The snapshot contains no audio buffer.
- Chart SVG viewBoxes are measured at actual pixel size. ResizeObserver redraws chart internals without replacing controls. Pitch follows a logarithmic 70-700 Hz scale; per-frame stroke width tracks level. Take dash patterns accompany numbers and colors.
- Playback cancellation resolves pending pair playback, so a stopped sequence cannot restart. Record, mode, picker and Delete actions stop the old source immediately. Motion off uses a glowing outline instead of a playhead.
- Line opens eight line chips in a keyboard-trapped dialog. Character and feeling tabs keep the short choice set in view. Plan dials move below the plot on desktop and remain in a two-column panel on phones. At 375 px, the chart follows the controls and is inspected by scrolling.
- Mystery order uses anonymous displayed numbers and neutral chart color. Its ordinary pickers and shelf are hidden. Guess choices show the complete character or feeling bank, not just the recorded answers. Reveal clears the working guesses; its temporary recap disappears when leaving Mystery.

#### Open question decided
The spec asks whether the site preview should allow microphone access or ask students to open full screen. No recommendation is explicit. This build keeps the existing no-mic Plan path and adds “Open full screen to record” when an embedding permission policy blocks the mic. The tool cannot grant itself iframe permission; no shared site template was changed.

#### Art and voice
All twelve paintings were made during this build with the built-in OpenAI image tool, with no people. The cream bubble, mouse and puppy were rekeyed with hole cleanup to remove green remnants. The voice manifest selects smooth-narrator (Algieba). Speech was not recorded, per the build brief; the kit uses browser speech fallback.

#### Spec discrepancy
The line “Shh. Something is coming.” has four words and only three internal word boundaries. The spec nevertheless offers four pauses on every line and requires the ghost gaps to fall between words. The build retains all five notches, fits only the three legal gaps for this line, and explicitly labels the three-of-four limit on the Plan stage. No within-word or trailing gap was invented. The owner should reconcile the four-pause notch with the shortest line. The other seven lines can fit all four pauses.

The newest chart is exactly twice the other chart heights. Whole card heights also contain fixed 44 px controls and full readouts, so the card height ratio is not exactly two. On phones, full plots are below the controls and require scrolling.

#### Audit closure
The single full audit completed in 1444 seconds with 19 leads. Four small Plan targets, four Card-label box overlaps, the phone studio-label overlap, two empty-picker names and three repeated-mode speech cuts were fixed. Two hidden-main-hint leads are expected behind modal dialogs, which provide their own instruction and focus trap. Three skipped-welcome leads follow the kit's explicit first-tap-own-line rule for Record, Clear and Change one thing.

Targeted checks using the same geometry routine are clean for 680, 800, 1000, 760, both phone modes, empty Compare and checked Plan at 680 and 1366. Repeated mode taps each speak one welcome without cuts. No full audit was repeated. The original extreme-state drag recipes omitted an outer return, so that audit did not actually move the dials. The recipes were corrected; separate timing-jittered real drags confirmed all four high values and the 7.818-second low-speed/four-pause extreme.

Final audio checks include actual Chrome fake-microphone capture at 220 and 330 Hz, a cancel-and-retry request with both tracks ending, five-take narration windows with no intrusions, plus direct PCM checks at both 70 and 700 Hz limits. A live classroom speech session remains for cold review. The source and bundle are readable, self-contained and under 2 MB; no host.html or owned Chrome/server remains.

All 5000 combinations of eight lines and four five-notch dials were checked. Duration arithmetic and the three relative bins match throughout; the maximum ghost is 7.8181818 seconds. Exactly 125 combinations, all using the four-word line and four requested pauses, encounter the documented three-gap limit. The final bundle is 521570 bytes, with 318572 bytes of art and 71 fixed voice lines.

#### Engine changes wanted
None. No kit, scripts, site or other tool files were edited. A site owner may separately choose allow="microphone" on its tool iframe.

#### Cold review changes
Plan checks now use the ghost's fixed 2.5 words/s speed reference, including when the student's usual take is faster.
Charts draw continuous paths, grouped into half-pixel loudness widths, with consistent dash phase; the ghost has rounded dots.
All range targets are 44 px high. Six feeling faces are matching shaded SVG icons rather than platform-dependent emoji.
The idle lamp was repainted with dark glass; its prompt and raw original are updated. No people images were added.
Mystery totals appear on the main stage; revealed-state hints and badges now reflect the revealed cards.
A non-usual first take is called a fallback baseline in both narration and chart labels, rather than called the student's usual voice.
Denied-mic hints survive card selections, card-family changes drop stale narration, and held R ignores repeat key events.
The audit recipes now include synthetic, analyzer-derived populated shelves, Compare, Mystery guessing and Reveal.
Cold-review evidence is in Scratch files beginning review-. The review report records the single final audit's result.

The cold audit completed in 1588 seconds with 12 mechanical leads. Its 85 frames were inspected. Default sizes,
repeat taps, rapid taps, Motion off and resize stress were clean. The documented leads concern modal hints,
history scrolling, phone charts below the controls, the drawing animation and correct first-tap welcome suppression.
The shelf recipe now waits 800 ms after its synthetic take arrives, past the specified 600 ms drawing animation.

Scoped corrections after that audit make the six-result Reveal recap a keyboard-focusable scrolling region,
and route Compare/Mystery playback feedback to the visible chart instead of the hidden Booth strip.
The line dialog speaks its own how-to once, drops it on close and delays a welcome until its controls are available.
Perform it now tells the listener to look away, both on screen and aloud; its instruction remains visible in compact layouts.
Those changes were re-shot at 680 and 1366, with phone recap frames, Motion-off playback and keyboard Space playback.
Five synthetic take events spoke one baseline result plus four take-result openings; each how-to spoke once.
One older comparison tail was correctly dropped when a newer take arrived. The final voice manifest has 74 matching lines.
Explicit NotAllowedError denial retained the Go to Plan hint after card selection, and Plan/Perform remained usable.
The final bundle is 524849 bytes. No owned Chrome, host listener or tools-folder host.html remains.

#### Verification
Numbers, screenshots, input scripts, audio-check results and audit output live in _scratch/character-voice-booth/.
codex-report.md documents the original build. codex-review.md records the cold review, fixes and latest audit.
One cold review pass, one final audit, then focused rechecks only. No commits or shared-file changes.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
