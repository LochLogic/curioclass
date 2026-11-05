# Codex report: cover-version-review

## Built
- Offline Listen, Measure and Review modes, with eight lyric columns and parallel A/B lanes.
- Beat-aligned A/B playback, synthesized vowel voice, guitar, brass and snare; piano reference; repeat sections.
- Tap tempo, per-line records, checked evidence, eight claim cards, playable pins, taste sliders and plain-text copy.
- Device-only persistence, confirmed reset, keyboard controls, Motion/Sound/Read and nine narration lines.
- Build only. No commits, shared-file edits, deployment or polish round. All owned test processes closed; host.html removed.

## Numbers check
- Scratch `numbers.json`: A upper-bound calculation 69.3679 seconds; actual linear easing 68.8215 seconds.
  This differs from the spec's rounded 69.4-second upper estimate but remains within its one-second tolerance.
- B: 10 eight-beat lines + 8-beat intro + 8-beat outro + 4-beat tag, at 120 bpm = 50 seconds.
- Actual full runs: A 68.8568 seconds; B 50.0852 seconds. No accelerated clocks.
- Four-tap, 30 ms Gaussian timestamp jitter, 20,000 trials: 100 percent within tolerance at 58, 99.435 percent at 120.
  The spec's 99.3 percent is consistent with a different simulation draw/model. Actual held clicks measured 59 and 123 bpm. Focused T-key taps measured 57 bpm for the 58-bpm line.
- Final runtime checks: T works with Tap tempo focused; repeat keys ignored; 29/241 discarded;
  30/240 accepted; a lost-beat gap resets the count; repeated A/B flips and live resize produce no errors.
- All 64 table values independently checked in Python. Perfect records: 48/48 counted cells; three planted errors: 45/48.
- WCAG ratios: ink/paper 15.55, ink/white 16.98, muted/paper 6.45, muted/white 7.05,
  brand/paper 6.15, white/brand 6.72, ink/A tint 14.15, ink/B tint 14.24.

## Feel check
- Best moment: flipping line 7 between A's slower held ending and B's brighter shifted key while keeping the beat and pin.
- Flat moment 1: the writer initially pushed its earned claim below the fold. Removed its redundant song header,
  kept both strip rows visible, and made compact evidence chips show all choices together.
- Flat moment 2: unknown and checked cells felt anonymous or crowded. Added lane labels on phones, a compact
  measurement selector and a small checked-value treatment that preserves the true values.
- Whole workflow exercised with real held inputs, full playback, measurements, claims, pin replay, copy and reset.
  Chrome was muted as required; subjective headphone timbre remains a review item.
- Compared against bundled Snowy Mail Route and Beat Lab copies in Scratch. `bar-comparison.png` places this tool
  beside Beat Lab. The finish is a paper record-review desk with detailed venue paintings and instrument cutouts.
![Cover Version Review beside Beat Lab](S:/CurioClass-codex/_scratch/cover-version-review/bar-comparison.png)

## Done when
1. PASS: central widest strip at 1366x768 and 680x425, both A/B rows visible; preview words give way to line numbers.
2. PASS: A/B preserves the beat, with a 30 ms crossfade and retimed active-note envelopes. Initial handler 2.5 ms;
   final repeated flips at most 0.4 ms. Column jump, reference-tune jump, intro flip and Stop tested.
   This verifies browser state and scheduling, not physical headphone output latency.
3. PASS: real 120 ms held taps at 58 and 120 with jitter read 59 and 123; three taps give the required prompt.
4. PASS: content-table and comparison checks agree; mismatches show off and the true value. Extras checked separately from count.
5. PASS: Add disabled without a pin and evidence; a Both pin played line 7 in A then B. Named pins play the named version.
6. PASS: real full playback lengths within one second of Sources, as above. Full runs preceded the final
   envelope/layout fixes; the beat-clock and sequence-length code stayed unchanged.
7. PASS: final voice retest heard all five claim events and one evidence how line across five repeats; no speech
   during music; Read stopped music. Same-mode quick taps preserve all three welcomes. No clips were recorded.
8. PASS: actual clipboard contains plain text, pin number and evidence after CRLF normalization; Reset removes saved work.

## Wave lessons
- Hint and voice: PASS. Hints update synchronously; no reliable evidence directs students to Measure; Read uses the current hint.
- Focus and layout: PASS. Stable buttons, preventScroll focus, reserved hint height and a confirmed reset dialog.
- Sizes: PASS. All STANDARDS sizes viewed; targeted checked cells, 760-pixel selector, 140-character words,
  compact evidence, 44-pixel targets and taste overlays verified. Phone lyric rows intentionally scroll.
- No giveaways: PASS. Measure starts unknown, Listen intentionally reveals values, and no score or right review judgment exists.
- Honest numbers: PASS. Tap count, bpm and the 8 percent window shown; unrecorded fields stay unknown.
- Standards: PASS. Re8 interpretation, Re9 criterion-backed pinned claims, Cn10 personal-taste sliders and comparison sentence.
- Motion off: PASS. Targeted playback frame reported zero running infinite animations; beat and word stepping remains.
- Short choices visible: PASS after compact evidence-chip layout and measurement selector; long saved claims may scroll.
- Resize mid-animation: PASS. Full audit reported clean; final live-resize and repeated-flip checks had no errors.
- Late welcome: PASS. No welcomeAfter; starting music hushes narration; mode welcomes are valid only while stopped.
- Unknown as unknown: PASS. Empty Measure and unsupported Review evidence render question marks.
- One look, one meaning: PASS. Lettered A/B badges, consistent tints, explicit off/check markers and selection outline.
- Badge true: PASS. Playback status updates with version and selected line; copied/saved messages reflect completed operations.
- Hint changes back: PASS. Mode, line, stop, reset and evidence changes recompute the current hint.
- No answer by copying words: PASS. Reviews require criteria and selected musical evidence; taste is not graded.

## Audit leads
- Full audit completed once in about 29 minutes: 36 leads. No audit time limit was hit.
- Read/soft/loud/preference targets: fixed with 44-pixel minimum button/select widths; focused geometry clean.
- Five instrument overlaps at 760: fixed by showing a complete selected measurement group; geometry clean.
- Because input name: fixed with explicit aria-label; focused geometry finds no unnamed controls.
- Unknown-cell overlaps: fixed with bounded line height; checked truth overlaps fixed with compact rendering and roomier rows.
- Taste controls below the short-window fold: fixed with a closing-card dialog; controls all visible at 1366, 680 and 375.
- Compact recorded-state focus: fixture had clicked a hidden group. Corrected selector/keyboard steps; real-input fixture passes.
- Reset covered keep regions: expected native modal behavior. Fixture now keeps the dialog, rather than its covered underlay.
- Phone lyric rows offscreen: intentional vertical strip required by the spec; transport/mode controls stay visible.
- Music-first welcome skipped on Play line/Play all/Plain: intentional; the spec makes it stale and forbids speech over music.
- Three quick-tap welcome cuts: fixed by treating an already-selected mode as a no-op; all three welcomed once without a cut.
- Full audit's resize and Motion-off checks were clean. All per-control held-click and five-repeat checks were clean.
- Focused final geometry checks found no overlaps, tiny text, small targets, unnamed controls or clipped controls in repaired states.
- The full audit was not rerun after fixes. Detailed dispositions: `_scratch/cover-version-review/audit-responses.md`.

## Frames looked at
- Bar frames, all eight art assets, all early/quick frames, all eight STANDARDS size frames including hosted 375.
- Measure, one/eight claims with 140-character text, grayscale, Motion off, keyboard and reset overlay frames.
- Every audit frame reviewed on contact sheets, with discovered problem states enlarged and targeted after fixes.
- Final focused frames: post-audit, overlay, last, and fixture-check folders. Includes native compact-record input,
  140-character wrapping, all three quick-mode states and all taste-dialog sizes. No browser console errors.

## Art made
- Eight built-in image-tool paintings, no redraws: two venues and six keyed instrument cutouts.
- Full prompts and provenance: `art/prompts.json`; originals: `art/raw/`; eight finished WebP files.
- Art 242.6 KB. Final bundle 427.8 KB, below 2 MB. All art used; no placeholders.

## Art still to paint
None. No people were generated.

## Engine changes wanted
Local formant, brass and snare voices plus an exposed per-player gain bus and beat seek/rate anchor for MS.play.
Exact files/functions and reasons are in handoff.md. No shared kit or family documentation was edited.

## Left open
- FAIL: an authenticated pre-1930 printing was not verified. The consulted Hudson engraving is modern, despite the
  Archive/Wikimedia 1848 catalogue date. The normalized eight-beat tune needs historical-printing verification before release.
- A line 8 contradicts itself: table says Voice only; prose says guitar drops out on the repeat. Followed the table,
  so both passes are Voice only. The repeated line plays; the contradictory guitar removal is not represented.
- Recorded calm-professor narration was not made, as instructed. Browser speech depends on locally available voices.
- Subjective headphone review of synthesized timbres remains open. No audio was recorded.
- No confirmed audit repair remains open after focused checks. The single full audit predates those fixes.
