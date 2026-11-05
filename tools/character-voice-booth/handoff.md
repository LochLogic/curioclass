# Character Voice Booth build handoff

## Structure
src.html starts from the kit starter and uses kit:curio CSS, Curio.voice, tones and Motion. There is no family engine. The single-file bundle is character-voice-booth.html. Build with CURIO_DRAFT=1. Twelve paintings are listed in art/prompts.json; originals are in art/raw and final WebP files are bundled through art tokens.

The script has content and narration tables, audio analysis, ghost generation, SVG charts, three mode renderers, capture and playback, then stable input handlers. window.__tool exposes the real state, analyzer and renderers for inspection. No test data is shipped. Scratch contains test-only PCM synthesis and Chrome fake-microphone checks.

## Tricky parts
- AudioWorklet captures mono Float32 chunks with microphone processing disabled. The embedded module is a data URL because Chrome rejects blob module loading under file URLs. The track is stopped after every take and cancellation. No MediaRecorder, network upload or persistence is used.
- Capture hushes narration before permission and disables Read through count-in, capture and analysis. Request tokens discard late permissions and canceled analysis. Count-in timing stays unchanged with Motion off.
- Analysis uses original 2048-sample windows at 10 ms hops. Samples within each frame are decimated to about 8 kHz for normalized autocorrelation over 70-700 Hz. A voiced frame requires above -45 dBFS and clarity at least 0.8. Five-frame median smoothing preserves unvoiced breaks. Speed assumes every word in the chosen line was spoken.
- Baseline is the latest My usual voice take, else the first remaining take. Deleting a baseline recalculates every readout. A seventh take preserves the baseline and drops the oldest other buffer. IDs never renumber, including after Clear.
- Plan uses the specified fixed usual speed of 2.5 words/s. A checked take retains a numeric snapshot of the reference used when recording started, so a new usual-voice take cannot move its own goalposts. The snapshot contains no audio buffer.
- Chart SVG viewBoxes are measured at actual pixel size. ResizeObserver redraws chart internals without replacing controls. Pitch follows a logarithmic 70-700 Hz scale; per-frame stroke width tracks level. Take dash patterns accompany numbers and colors.
- Playback cancellation resolves pending pair playback, so a stopped sequence cannot restart. Record, mode, picker and Delete actions stop the old source immediately. Motion off uses a glowing outline instead of a playhead.
- Line opens eight line chips in a keyboard-trapped dialog. Character and feeling tabs keep the short choice set in view. Plan dials move below the plot on desktop and remain in a two-column panel on phones. At 375 px, the chart follows the controls and is inspected by scrolling.
- Mystery order uses anonymous displayed numbers and neutral chart color. Its ordinary pickers and shelf are hidden. Guess choices show the complete character or feeling bank, not just the recorded answers. Reveal clears the working guesses; its temporary recap disappears when leaving Mystery.

## Open question decided
The spec asks whether the site preview should allow microphone access or ask students to open full screen. No recommendation is explicit. This build keeps the existing no-mic Plan path and adds “Open full screen to record” when an embedding permission policy blocks the mic. The tool cannot grant itself iframe permission; no shared site template was changed.

## Art and voice
All twelve paintings were made during this build with the built-in OpenAI image tool, with no people. The cream bubble, mouse and puppy were rekeyed with hole cleanup to remove green remnants. The voice manifest selects smooth-narrator (Algieba). Speech was not recorded, per the build brief; the kit uses browser speech fallback.

## Spec discrepancy
The line “Shh. Something is coming.” has four words and only three internal word boundaries. The spec nevertheless offers four pauses on every line and requires the ghost gaps to fall between words. The build retains all five notches, fits only the three legal gaps for this line, and explicitly labels the three-of-four limit on the Plan stage. No within-word or trailing gap was invented. The owner should reconcile the four-pause notch with the shortest line. The other seven lines can fit all four pauses.

The newest chart is exactly twice the other chart heights. Whole card heights also contain fixed 44 px controls and full readouts, so the card height ratio is not exactly two. On phones, full plots are below the controls and require scrolling.

## Audit closure
The single full audit completed in 1444 seconds with 19 leads. Four small Plan targets, four Card-label box overlaps, the phone studio-label overlap, two empty-picker names and three repeated-mode speech cuts were fixed. Two hidden-main-hint leads are expected behind modal dialogs, which provide their own instruction and focus trap. Three skipped-welcome leads follow the kit's explicit first-tap-own-line rule for Record, Clear and Change one thing.

Targeted checks using the same geometry routine are clean for 680, 800, 1000, 760, both phone modes, empty Compare and checked Plan at 680 and 1366. Repeated mode taps each speak one welcome without cuts. No full audit was repeated. The original extreme-state drag recipes omitted an outer return, so that audit did not actually move the dials. The recipes were corrected; separate timing-jittered real drags confirmed all four high values and the 7.818-second low-speed/four-pause extreme.

Final audio checks include actual Chrome fake-microphone capture at 220 and 330 Hz, a cancel-and-retry request with both tracks ending, five-take narration windows with no intrusions, plus direct PCM checks at both 70 and 700 Hz limits. A live classroom speech session remains for cold review. The source and bundle are readable, self-contained and under 2 MB; no host.html or owned Chrome/server remains.

All 5000 combinations of eight lines and four five-notch dials were checked. Duration arithmetic and the three relative bins match throughout; the maximum ghost is 7.8181818 seconds. Exactly 125 combinations, all using the four-word line and four requested pauses, encounter the documented three-gap limit. The final bundle is 521570 bytes, with 318572 bytes of art and 71 fixed voice lines.

## Engine changes wanted
None. No kit, scripts, site or other tool files were edited. A site owner may separately choose allow="microphone" on its tool iframe.

## Cold review changes
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

## Verification
Numbers, screenshots, input scripts, audio-check results and audit output live in _scratch/character-voice-booth/.
codex-report.md documents the original build. codex-review.md records the cold review, fixes and latest audit.
One cold review pass, one final audit, then focused rechecks only. No commits or shared-file changes.
