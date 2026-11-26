# Cover Version Review: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: cover-version-review

#### Built
- Offline Listen, Measure and Review modes, with eight lyric columns and parallel A/B lanes.
- Beat-aligned A/B playback, synthesized vowel voice, guitar, brass and snare; piano reference; repeat sections.
- Tap tempo, per-line records, checked evidence, eight claim cards, playable pins, taste sliders and plain-text copy.
- Device-only persistence, confirmed reset, keyboard controls, Motion/Sound/Read and nine narration lines.
- Build only. No commits, shared-file edits, deployment or polish round. All owned test processes closed; host.html removed.

#### Numbers check
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

#### Feel check
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

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
- Bar frames, all eight art assets, all early/quick frames, all eight STANDARDS size frames including hosted 375.
- Measure, one/eight claims with 140-character text, grayscale, Motion off, keyboard and reset overlay frames.
- Every audit frame reviewed on contact sheets, with discovered problem states enlarged and targeted after fixes.
- Final focused frames: post-audit, overlay, last, and fixture-check folders. Includes native compact-record input,
  140-character wrapping, all three quick-mode states and all taste-dialog sizes. No browser console errors.

#### Art made
- Eight built-in image-tool paintings, no redraws: two venues and six keyed instrument cutouts.
- Full prompts and provenance: `art/prompts.json`; originals: `art/raw/`; eight finished WebP files.
- Art 242.6 KB. Final bundle 427.8 KB, below 2 MB. All art used; no placeholders.

#### Art still to paint
None. No people were generated.

#### Engine changes wanted
Local formant, brass and snare voices plus an exposed per-player gain bus and beat seek/rate anchor for MS.play.
Exact files/functions and reasons are in handoff.md. No shared kit or family documentation was edited.

#### Left open
- FAIL: an authenticated pre-1930 printing was not verified. The consulted Hudson engraving is modern, despite the
  Archive/Wikimedia 1848 catalogue date. The normalized eight-beat tune needs historical-printing verification before release.
- A line 8 contradicts itself: table says Voice only; prose says guitar drops out on the repeat. Followed the table,
  so both passes are Voice only. The repeated line plays; the contradictory guitar removal is not represented.
- Recorded calm-professor narration was not made, as instructed. Browser speech depends on locally available voices.
- Subjective headphone review of synthesized timbres remains open. No audio was recorded.
- No confirmed audit repair remains open after focused checks. The single full audit predates those fixes.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: cover-version-review

#### Played

Cold as a grade 7 student, then as a teacher projecting the strip. Played Listen, Measure, checked records, Review and taste before reading builder notes or source. The A/B contrast and illustrated record-desk world are strong; the blank review and tiny checked feedback were flatter.

#### Findings fixed

- Blocker, general, Measure/Review: a single guessed field exposed all four answers, including an untapped tempo. Real held clicks reproduced it. Checks now expose only explicitly attempted fields; unchecked guesses no longer unlock evidence.
- Blocker, general, comparison: trying choices after seeing truth replaced a miss with a perfect comparison. First checked responses now persist through corrections and Clear taps, including the denominator. Corrections remain useful evidence, clearly separate from that initial record.
- Should fix, general, Review: blank claims and identical duplicates could fill the review without explaining anything. A Because explanation is required; exact duplicates stay disabled and changing criterion recomputes eligibility.
- Should fix, general, tapping: a partial, lost-beat or discarded retry could reuse a previous matching bpm. A fresh attempt clears and saves removal of the old estimate; invalid/lost attempts clear it too.
- Should fix, general, playback: A's line 7 ending was a short note, despite the held-note label. Lines 4 and 7 now sustain their final pitch over beats 6 through 8; the final word lights on those beats in both versions.
- Should fix, general, voice: a picker change dropped the fifth queued saved-claim announcement. Picker changes now drop stale how-to lines while preserving valid saved-claim events; deleted claims invalidate their pending event.
- Should fix, general, craft: narrow corner copy clipped and Version options truncated. Compact corner spacing and A/B/Both labels now fit. Replay synchronizes the draft pin; preferences credit the other version.
- Should fix, general, compact Review: the audit confirmed the first saved pin below the 680x425 fold. The newest playable claim now replaces the evidence row in short previews; tapping a lyric line restores its evidence choices. The native range/dialog return-focus path also has a guarded fallback.
- Should fix, general, modal voice/craft: Reset as the first tap could narrate Listen over its confirmation. Welcomes now wait until dialogs close. Taste tracks now span their endpoint labels with 44-pixel targets. Singular tap/cell/beat wording and copy feedback when storage is blocked were corrected.
- Polish, general: Check gives a restrained lane reveal instead of only changing a number; repeats identify themselves in the transport. Redrew the weakest art, the trombone, with an unmistakable long slide.

#### Findings left

- Should fix, source/spec conflict: no authenticated pre-1930 printing verified. The cited Hudson score is a modern engraving. Preserved the explicit transcription limitation instead of claiming the normalized reference is historically verified.
- Nit: My taste repeats its heading inside the closing card. Left intact.

#### Break it

- Empty Check is disabled. One loudness guess no longer reveals tempo, instruments or extras. Wrong -> Check -> correct -> Check keeps the original miss; clearing a wrong tempo cannot shrink the denominator.
- Review offers only checked fields; cycling unchecked options reveals no correctness. No pin, no chip or no explanation blocks Add. Exact duplicate blocks; eight-claim and 140-character states inspected. Interpretations and personal taste are not automatically graded.
- Real held taps at 58 and 120 bpm matched within 8 percent; three taps requested a fourth. Fast 100 ms tapping, lost-beat gaps and partial retries could not retain old bpm. Exact 30/240 boundaries accepted; 29/241 discarded.
- Both-version pin played A then B. Copy retained line numbers and evidence, actual clipboard checked. Reset cleared measurements, first comparisons, claims and preferences. Slider extremes do not earn a score.
- Listen intentionally shows reference values. Copying those can produce a matching record; this is an open listening/explanation tool, not a secure assessment. No score, best score or mastery award is claimed.

#### Voice walk

Held clicks at a two-second pace: lyric 1 -> Play line -> A/B -> Stop -> Measure -> Play line -> Stop -> loudness -> Check -> Review -> Version B -> lyric 1 -> evidence -> explained claims -> Both pin -> Read -> Sound off/Read -> Reset.
Heard in order: welcomeListen, welcomeMeasure, checkDone, welcomeReview, needEvidence, five claimAddedSingle events, claimAdded, Read. Welcome starts are interrupted when the student starts music; no narration waits ahead of playback.

| Line | Kind | Expected | Heard |
|---|---|---|---|
| Each mode welcome | how/welcome | once | 1 each |
| needEvidence | how | once across repeats | 1 |
| claimAddedSingle | event | five | 5 |
| claimAdded | event | once for Both | 1 |

Read stopped music and worked with Sound off. No fixed lines were added; lines.json still matches allLines. Browser speech is used, with no recorded calm-professor takes; subjective headphone timbre remains open.

#### Facts checked

- Brackett Jr., 1848, Alfred, Maine, Shaker dance song: [Canterbury Shaker Village finding aid, p. 4](https://www.shakers.org/wp-content/uploads/2020/05/ROGER-LEE-HALL-COLLECTION-Canterbury-Shaker-Village.pdf).
- Eight lyric lines and religious dance context: [Roger Lee Hall, Joseph Brackett's Simple Gifts](https://www.americanmusicpreservation.com/JosephBrackettSimpleGifts.htm). No Copland arrangement reproduced.
- Copland used the tune in Appalachian Spring, premiered in 1944 with Martha Graham: [Library of Congress](https://blogs.loc.gov/loc/2014/10/documenting-dance-the-making-of-appalachian-spring/).
- Meaning of cover version: [Oxford Learner's Dictionary](https://www.oxfordlearnersdictionaries.com/us/definition/english/cover-version).
- Interpret expressive intent, apply criteria, connect preference: [NCAS Music at a Glance](https://nationalartsstandards.org/sites/default/files/Music%20at%20a%20Glance%20rev%2010-2-14.pdf). Student actions: criterion-backed playable claims, interpretation, taste and comparison sentence.
- Fictional performers, all 64 content-table fields, keys, repeats, dynamics, instruments, 8 percent rule: spec Content/Sources, independently compared with source table. Numbers in review-numbers.json.
- A upper bound 69.3679 s; linear easing 68.8215 s. B 100 beats at 120 bpm = 50 s. Actual full plays: 68.8349 s and 50.1025 s. Four-tap 30 ms jitter, 20,000 trials: 100 percent at 58, 99.54 percent at 120. Contrast: ink/paper 15.55:1, muted/paper 6.45:1, white/brand 6.72:1, ink/A 14.15:1, ink/B 14.24:1.
- Historical source requirement remains unverified: [IMSLP Hudson #52769](https://imslp.org/wiki/Simple_Gifts_(Brackett,_Joseph)) identifies the consulted modern score. It cannot establish a pre-1930 printing.

#### Sensitivity

Shaker religious dance song. A cultural reviewer should check songwriter/community credit, the origin of the words, and that fictional Porch/Parade treatments are not presented as Shaker performance practice. Questions about simplicity must not make either arrangement morally or culturally superior. Notes and handoff now name this. All eight illustrations depict objects/empty venues, with explicit people:false.

#### Flattest moment left

Writing the Because explanation is still the slowest moment. Kept it: interpreting evidence is the skill. Check now visibly reveals attempted lanes, and repeated passages identify themselves. The compact first pin is now immediately playable instead of hidden below the writer. The expressive A/B contrast and playable pins remain the payoff.

#### Graphics

Inspected all eight WebP images and their rendered sizes. Kept both rich venue sleeves and five other cutouts; replaced only the ambiguous trombone. Built-in imagegen replacement is art/trombone.webp, with its raw PNG and prompt in art/raw/ and art/prompts.json; predecessor retained in Scratch. No placeholders or missing art tokens. Final art 246,666 bytes; bundle 442,136 bytes (431.8 KiB). Opened both approved bar tools from existing Scratch bundles; retained this tool's own visual identity.

#### Audit

Completed once within the 40-minute limit: eight leads. Four are the specified scrolling phone strip, three are intentional music-first welcome suppression, and one was the confirmed compact saved-pin flaw, now fixed. No second full audit.
Inspected all 40 audit frames, with full-size lead frames and seven labelled sheets. Controls, five-click/quick-tap narration, Motion off and resize stress checks were clean. Re-shot compact pins at 680/800/1000, all three affected taste sizes, modal voice, continuation/replay, singular wording and blocked storage. Final hosted phone run: zero errors.
The initially failing custom focus fixture had no active range. Real held-click mode entry, native End and dialog close now pass. Final validation has 16 passing checks; all owned Chrome/host ports are closed and host.html is removed. Evidence: review-validation.json, review-audit-dispositions.md, post-audit-frames/, voice-recheck/voice-main.json and the original cheap-before.json, all in this tool's Scratch folder.

#### Left open

Authenticated historical printing and corresponding exact melody/rhythm comparison. No invented edition or unsupported historical-transcription claim added.
A line 8 spec conflict remains: table says Voice only, prose says guitar disappears on the repeat. Kept the explicit table rather than inventing an instrument change.
Browser speech cannot demonstrate the selected recorded bank voice; no recording was authorized. Physical headphone timbre/latency was not measured in muted Chrome.
One cold pass and focused rechecks only. No commits, no shared-file changes, no deployment. All evidence is in this tool's Scratch folder.
Process deviation: the first four read-only commands completed immediately with tool yield limits, before the enforced-deadline wrapper was installed. Subsequent shell commands had enforced deadlines. A full-A test first hit the driver's 60-second per-evaluation limit; the smaller retry completed without accelerating playback.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Cover Version Review: build handoff

#### Structure
One offline source, `src.html`, using kit:curio and kit:music-studio.
CSS defines the record-sleeve desk, a responsive difference strip, the transport and each mode's controls.
The script contains the content table, melody, persistence, voice queue, strip, measurement model,
review writer and two gain buses. `window.__tool` exposes state and focused verification hooks.
Controls precede the eight line buttons in DOM tab order. CSS places the strip first on desktop.
At 375 pixels, lyric lines become rows and A/B sit side by side; playback and recording controls stay above them.
Compact measurement windows use a selector to show each complete group of recording choices.
My taste opens as a native closing-card dialog so both sliders and the sentence controls stay visible together.
The Review writer keeps My taste and Copy review next to Add claim, including on phones.

#### Tricky parts
- A/B crossfades gain buses over 30 milliseconds. Both buses use a shared beat position, with the audible
  version setting the rate. The switch preserves that beat, not elapsed seconds.
  Active vowel/brass envelopes are retimed to the new version's remaining beat duration when it flips.
- A's last two beats on lines 4 and 7 ease linearly to 80 percent of the listed tempo.
  The clock integrates that curve analytically. Real full plays measured 68.86 and 50.09 seconds.
- The local scheduler uses the page clock and short Web Audio dispatches. MS.parse supplies pitch events;
  MS.pluck supplies guitar and the engine's piano voice supplies Plain tune. Local formant, brass and snare
  implementations are in the source because the shared kit is read-only during this build.
- During music, narration stays silent. Events are deferred to stop. Repeated event instances get unique
  queue keys so a newer claim does not erase an earlier pending claim. Read stops music first.
- Measurements and checks are per field, line and version. Check never exposes an unattempted field.
  `checked[k]` stores attempted values by field; old boolean checks migrate only fields actually recorded.
  `firstChecks[k]` preserves first responses, so exposed answers cannot erase a miss. The count excludes extras.
  This compares a record; it does not score listening skill.
- Review evidence requires an explicitly checked field. It does not reveal whether an unchecked guess matches.
  A Because explanation is required, and exact duplicate claims are disabled. Interpretations are not auto-graded.
  A Both pin plays A and then B. A named-version pin plays only that version.
- All saves are wrapped localStorage calls. Reset uses a native dialog with a safe initial focus and clears
  every saved field. Clipboard has a plain-text fallback. Nothing is recorded or sent anywhere.

#### Spec choices and open questions
- Voice: kept calm-professor / Schedar, as the spec leans. Its use in a different grade's gallery tool does
  not override this explicit selection. No recording was made; the kit uses browser speech until later narration work.
- Engine conflict: followed CODEX-BUILD's ban on kit and docs changes. Implemented the required extra synth
  voices locally, with the shared change request below.
- Historical printing: no authenticated pre-1930 printing was verified. The Archive/Wikimedia item with an
  1848 catalogue date is a Robert A. Hudson modern engraving with Finale PrintMusic 2009 metadata.
  The supplied public-domain melody was implemented with pickups inside each lyric column and durations
  normalized to eight beats. Notes name the consulted score and the Chambers pitch reference.
  Verification against an authenticated printing remains open. Do not treat this as a verified historical transcription.
- A line 8: the table specifies Voice only, while the prose says the second repeat removes guitar.
  Followed the explicit instrument table: Voice only on both passes. The repeated line is audible, but there
  is consequently no guitar removal between its passes. This contradiction remains for the owner/reviewer.
- Slowdown: used the specified gradual easing, rather than holding the final two beats at 80 percent throughout.
  Recomputed duration 68.82 seconds versus the supplied 69.4-second upper estimate, within its one-second tolerance.
- Repeat clips: Play line plays one eight-beat line for short comparison. Play all performs the additional
  repeats, B's intro/outro and tag. Switching from B's non-lyric intro/outro to A starts the selected lyric line,
  since A has no corresponding instrumental section.
- Extra labels abbreviate only in short previews (held, slows, repeat, shout, key up arrow).
  Their title text and the Measure controls keep the full names.
- Added a matching claim-added voice variant for a named-version pin: it says "this version" instead of
  "both versions". STANDARDS requires the spoken line to match the actual playback. Empty pins without
  reliable evidence direct the student to Measure and do not speak the unavailable evidence-chip instruction.
- Check uses a compact two-line result per lane. In short previews, the off badge sits beside the true value
  to preserve legibility. Full windows put the true value beneath the recorded value.

#### Art
Eight generated paintings, all present and used: two venue sleeves and six instrument cutouts.
Cold review redrew the trombone with a recognizable long slide; the original is retained in Scratch.
Full prompts and provenance are in `art/prompts.json`; raw originals are in `art/raw/`.
The images contain no people. No artwork remains to paint.

#### Engine changes wanted
- `kit/music-studio.js`, instrument functions / INSTR: add formant ah and oo voices using two bandpass formants,
  filtered sawtooth brass voices and a snare noise envelope. Preserve existing instrument calls.
- `kit/music-studio.js`, play(): expose or accept a per-player gain bus and support a beat-aligned seek / rate
  anchor. The current private bus prevents direct use of MS.play for a 30-millisecond A/B crossfade.
- Update `docs/families/music-studio.md` with those APIs in the same shared change. No shared files were edited here.

#### Verification pointers
Evidence, bar copies, screenshots and timeout wrappers are under `_scratch/cover-version-review/`.
`functional.json` records real held taps, comparison cells, pin playback, full durations and reset.
`voice-check.json` records repeat narration. `clipboard-check.json` records the corrected real clipboard check,
including Windows line-ending normalization. `static-check.json` checks all 64 content fields.
The final report records the audit outcome and any remaining limitations. This was Build only, without a commit.

#### Audit dispositions
The single full audit completed with 36 leads. Post-audit focused checks cover its confirmed fixes: 44-pixel minimum
widths, explanation-input name, unknown/check lane spacing, 760-pixel instrument layout, the taste dialog, long-word
wrapping and same-mode clicks preserving a welcome already in progress. The compact recorded-state fixture now
opens the measurement selector before choosing loudness. Modal fixtures keep the modal itself in view.
Phone lyric rows intentionally scroll as the spec requires. A music-first tap intentionally suppresses the welcome
so narration cannot overlap music. The full build audit was not rerun after the builder's targeted fixes.

#### Cold review changes
- Real held clicks reproduced answer flooding, overwrite-to-perfect feedback and a blank tempo claim without tapping.
  Repaired those paths with per-field checking, first-response preservation and the explanation requirement.
- A fresh tap attempt clears and saves removal of the previous tempo. Lost or invalid attempts cannot reuse it.
- A's final notes on lines 4 and 7 now occupy beats 6 through 8. The final word lights for those beats in both versions;
  flipping preserves the displayed word. `soundLog` records held-note events for verification.
- Repeat sections identify themselves in the transport. Check visibly reveals attempted lanes; Motion off removes the effect.
- Narrow strip-corner copy and Version choices were made readable. Preference selectors credit the other version.
- Replay pins synchronize the draft pin and clear stale evidence. No kit, scripts or shared docs changed.
- The review audit confirmed that a first claim's pin was below the 680x425 writer fold. At heights up to 650 pixels,
  `body.showing-claim` swaps the evidence row for the newest playable claim, with full text in its title and DOM.
  Tapping a lyric line clears the class and restores all evidence choices. The strip and transport stay in place.
- The dialog close handler restores focus on the next frame, with a guarded 100-millisecond fallback only if focus
  otherwise fell to the body or the closed dialog. The final held-click mode entry, native End key and dialog-close
  path passes. An earlier custom fixture sent input before the mode's controls were painted; it had no focused range.

#### Sensitivity
Shaker religious dance song: check attribution to Elder Joseph Brackett Jr., 1848, and distinguish invented modern
performances from Shaker practice. All eight assets contain no people and explicitly have `people: false`.
The pre-1930 printing requirement remains unresolved; the modern score does not verify a historical printing.

#### Cold review audit and final evidence
The one review audit completed within its 40-minute limit with eight leads. Four were the specified scrolling phone
strip, three were intentional music-first welcome suppression, and one was the confirmed compact saved-pin issue.
The compact pin repair passes at 680x425, 800x500 and 1000x625; pin replay and returning to evidence choices pass.
All 40 audit frames were inspected. Audit controls, repeated narration, Motion off and resize stress checks were clean.
The semantic Reset-dialog welcome mismatch, full-width 44-pixel taste tracks, singular wording and truthful blocked-save
feedback were also repaired. A data favicon keeps the tool self-contained. The temporary host's favicon metadata had to
precede its iframe; the final hosted phone run has zero errors. No shared host or script was edited.
Final evidence: `_scratch/cover-version-review/review-validation.json`, `review-audit/audit.md`, `post-audit-frames/`,
`voice-recheck/voice-main.json`, `review-numbers.json`, `full-A-review.json`, `full-B-review.json`, and `end-focus-final.json`.
Full plays measured 68.8349 seconds for A and 50.1025 for B. Historical-printing verification remains open.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
