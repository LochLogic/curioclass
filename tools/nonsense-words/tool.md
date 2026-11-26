# Nonsense Words: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: nonsense-words

#### Built
Offline Explore, Practice test and Challenge, preserving the owner-supplied 200-word bank. Quiet parchment, blue outer border and one still quill follow the owner's Look decision. Flags, last mode, kinds and per-kind-mix best scores persist on device. No git commits, polish round or changes to sibling source files.

#### Numbers check
PASS: 114 CVC + 50 CVCe + 36 letter-pair words = 200 unique entries. Embedded bank matches words.txt character-for-character and in order. Scratch/check_bank.py and numbers.json hold the independent check. Practice thresholds are 2,000 and 4,000 ms; Challenge cap is 60,000 ms. Thirty-word sessions always have enough entries, including the smallest kind of 36.

#### Feel check
Best moment: finishing a mixed practice run and opening exactly its Not yet and skipped words in Explore. The 30-of-30 banner also feels earned, with a brief cheer and optional confetti.

Two flattest moments were the cramped compact hourglass/counter area and an end screen whose review was squeezed behind too many settings. The build now reserves the reading area, fixes explicit grid rows, and hides settings on results so score and review stay legible. Ordinary reading deliberately stays quiet and still.

Played the full Explore, mixed Practice, retry and Challenge paths, including a real keyboard-only 20-word run. This is a teacher-supported drill, not a game: the person listening supplies the feedback. Scratch/bar-comparison.jpg places its 1366 frame beside Snowy Mail Route. Both bar tools were bundled only in Scratch and opened. This tool is visibly plainer by the owner's explicit decision. No richness or gameplay was added to override that decision.

#### Done when
- PASS: all three modes work. Functional checks cover every session length, scoring, skips, flags, review, shuffle and deadline rejection; real held clicks cover the compact repair. functional-results.json has 38 passing assertions.
- PASS: exactly words.txt, filtered by the three kinds toggles. Counts and group boundaries were verified independently and in Chrome.
- PASS: Practice never advances on its own. A real wait confirmed green initially, yellow after 2.1 seconds, red after 4.3 seconds, same word and index. Marking resets the hourglass immediately.
- PASS: far below 2 MB. Final bundle is approximately 69 KB, with 5.3 KiB of art and no recorded audio.

Additional evidence: a real 62-second Challenge check was running at 31 seconds and done at 62 seconds; late marks are independently rejected by the deadline check. Keyboard-only Tab, Enter and arrows finished a 20-word practice run with focus on Again. F, R and N handlers were checked too. localStorage persistence and blocked-storage fallback work. No target word is ever spoken by the tool.

#### Wave lessons
- PASS, Hint and voice: hints change synchronously, name available controls, and Read uses the current hint. Curio.voice holds six instruction/cheer lines. At a 2-second held-tap pace the instructions start once per step and ordinary score taps do not narrate. Start intentionally interrupts the ready-screen invitation. No target words are spoken.
- PASS after repair, Focus and layout: controls stay in the DOM, no focus on load, preventScroll on deliberate focus moves. Empty compact secondary-action boxes no longer cover Start. Held-click checks at 680, 800 and 1000 reach word 3 with focus on Not yet.
- PASS, Sizes: all eight STANDARDS sizes, including 375x812 in an iframe, have visible primary controls. Main controls are 60 px; compact kit utility controls are 44 px. Initial size audit was clean. Targeted repair frames were viewed.
- PASS, No giveaways: the tool does not supply pronunciations or automatically assess a spoken answer. Right and Not yet are the listener's judgment.
- PASS, Honest numbers: score denominators are session totals, skips count as specified, and unreached Challenge words are labeled separately. Bests compare the same kind mix.
- PASS, Standards: the actual reading task exercises CVC/CVCe decoding for the specified RF.2.3a focus. No family engine is named or needed. This is explicitly partner-supported practice.
- PASS, Motion off: no infinite animation; perfect-run confetti is absent, timers remain unchanged. Finished assets are embedded, not placeholders.
- PASS, Short choices visible: all three kinds and all three session lengths remain in view. Long review/flag lists may scroll; the primary controls do not.
- PASS, Resize mid-action: timer and deck state do not depend on drawing geometry. Audit resize result is recorded below.
- PASS, Deferred welcome: no welcomeAfter. The current mode and phase determine a valid instruction; Read stops the queue.
- PASS, Unknown stays unknown: there is no automatic assessment or diagnostic label. The learner and listener decide the mark.
- PASS, One look one meaning: Right has a check and green tint; Not yet has a cross and red tint. Hourglass color also has a text cue. Grayscale frame was inspected.
- PASS, Badge truth: flag and counter reflect current state; result scores and bests come from actual marks.
- PASS, Hint changes back: mode switches, ready/running/done and focused review all set the hint immediately.
- PASS, No answer by copying words: no model pronunciation, answer card or hidden-answer clue exists.

Nominal palette contrast ratios: ink/parchment 12.06:1, muted/parchment 5.82:1, white/blue 8.75:1, Right 6.90:1 and Not yet 6.38:1. Selected hover controls now keep white text on dark blue.

#### Audit leads
Completed once, exit 0, with 40 grouped leads. Evidence: Scratch/audit/audit.md. All 81 audit PNGs were inspected in audit-contact/sheet-00.jpg through sheet-14.jpg.

- Two flags-open keep-region leads: intentional. A native modal covers the reading area and its underlying hint. The modal has its own instructions, a visible Close button, keyboard Escape and focus containment. Frames confirm this at every size.
- Six practice-running leads: fixed. Three focus-loss and three hidden-control rows came from the empty compact secondary-controls container intercepting Start. It is now hidden whenever all its buttons are hidden. Held clicks at 680x425, 800x500 and 1000x625 start the run, advance two words and retain focus on Not yet.
- Fourteen practice-results leads: fixed by the same hit-area repair. The missed Start meant all ten following Not yet taps were on hidden controls, so results were never reached. A new real-input 10-word compact run reaches results and opens its exact review subset.
- Fourteen review-subset leads: fixed by the same repair. The missed Start caused ten skipped-input misses, a missed Practice these tap and two hidden keep regions. The targeted review path now reaches Explore with exactly ten review words; All is visible. Skip and review semantics also passed the functional checks.
- One first-tap Flagged welcome lead: the reading instruction is intentionally withheld while the modal is up. Closing the dialog now retries the unheard welcome. A fresh-profile held-click Flagged then Close check logged one spoken Explore instruction and returned focus to Flagged.
- Three quick-kind speech-cut leads: fixed. Kind changes refresh deck, counter and hint without hushing a still-valid generic instruction. A six-tap test toggled every kind off/on at 0.7-second gaps, then waited nine seconds. It logged one uninterrupted instruction and restored all 200 entries.

The audit's size checks, Motion off check, ordinary control/Enter paths, five-click checks and resize stress checks otherwise passed. No console exceptions were found. A selected-hover contrast repair and preservation of the current mode were also verified with targeted held input. Re-tapping a running Challenge preserved its first mark; rapid repeats of the Practice mode did not cut its invitation.

Some audit sections were captured before these repairs. The final bundle has targeted rechecks, not a second full audit. The audit's iframe host used its original snapshot. No polish round was started.

#### Frames looked at
All screenshots in early-frames, sizes-frames, modes-frames, phones-frames, functional-frames, targeted-frames, results-fix-frames, timeout-retry-frames, post-audit-fixes-frames, voice-recovery-frames, mode-repeat-frames and kind-quick-frames were viewed individually or in labeled contact sheets. Both bar frames and bar-comparison.jpg were viewed. Standard sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe. Modes include ready, running, red hourglass, flags dialog, results, review, timeout, perfect, grayscale, keyboard and Motion off. Audit contact sheets enumerate the audit frames viewed.

#### Art made
Two built-in image_gen images: art/parchment.webp and art/quill.webp, 5,450 bytes total (5.3 KiB). No redraws. Full prompts and house style are in art/prompts.json; raw originals are in art/raw. Finished art was inspected at final size. No people or characters. Browser voice uses 0 KB of recorded audio. Bundle bytes: 70,626 bytes (69.0 KiB).

#### Art still to paint
None.

#### Engine changes wanted
None. All repairs are in this tool's CSS and logic.

#### Left open
- Owner approval of words.txt before shipping. The bank is unchanged; handoff.md lists possible real words, sound-alikes, a name and an unverified multilingual wording concern.
- Browser speech is allowed by the spec until voice night; no recordings or listening review were made. Muted Chrome checked speech scheduling only.
- The full audit was not rerun after the compact hit-area, selected-hover, dialog welcome recovery, current-mode preservation and quick-kind speech fixes. Targeted real-input checks verify the fixes; a cold review is next.
- No classroom trial was performed. No polish round was started.
- The first real-time test's result was sampled before its screenshot wait, so it was not treated as deadline proof. A second attempt hit CDP's 60-second request cap; the smaller split-wait retry succeeded. Early host favicon 404s were removed with an inline icon and the host recheck was clean.

All started Chrome instances and servers were closed. Temporary host.html was removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: nonsense-words

#### Played
Simulated a grade 2 reader and projector teacher: Explore, flags, mixed Practice, review, perfect Challenge and a real one-minute timeout. Played before reading builder reports, notes or source. The quiet reading space fits the brief.

#### Findings fixed
- **Should fix, general, Explore:** the opening hint and welcome named disabled Back. Instructions now name available controls at the first, last and single-review-word boundaries.
- **Should fix, general, compact controls:** Sound, Motion and Read were 44 px tall. All now retain the grade-band 60 px target.
- **Should fix, general, perfect result:** the 680x425 panel clipped the personal best. Short previews keep the wide banner, score and best; a redundant heading yields room, with tighter paragraph spacing. Larger results retain their headings. Added #best to that audit state's keep list.
- **Should fix, general, Read:** four fixed hints were absent from the narration catalog. All 12 instruction lines now match allLines and voice/lines.json. Marking hints use words without spoken check/cross glyphs.
- **Should fix, general, Flagged:** reopening the picker while its closing welcome played cut that instruction permanently. Only an interrupted welcome is rearmed; the next Close plays it whole. Fully heard instructions stay quiet.
- **Polish, general, mode navigation:** added the control-group role, so the audit discovers and walks both timed modes.
- **Polish, general, Practice ending:** replaced generic encouragement with the actual attempt count and specific review count.
- **Polish, general, parchment:** visible repeating squares weakened the otherwise appropriate art. Rendered the existing paper once at cover size, removing seams while retaining texture.
- **Polish, general, notes:** added a concrete supportive response to Not yet: blend taught sounds together and retry in Practice these.

#### Findings left
No in-scope blocker or should-fix remains. The unchanged bank still needs the owner's specified approval before shipping.

#### Flattest moment left
Ordinary Next remains a quiet, repeated action, as the owner's Look requires. The listening partner supplies reading feedback. The formerly generic Practice ending now points to this reader's specific review set.

#### Graphics
Both finished assets inspected: 640 px parchment and 80 px quill, including their displayed sizes. Retained both, 5,450 bytes total; no missing art or people. Improved the weakest rendering, the tiled paper, without adding illustrations.
Final bundle: 71,692 bytes, about 70 KiB. Blue border, centered word, still header flourish and Sight Words sibling structure preserved. Viewed both bar tools' existing bundles; the owner's plain Look takes precedence.

#### Audit
One full audit completed with exit 0 under the 40-minute limit, Chrome 9961 and host 8765. Evidence: _scratch/nonsense-words/review-audit/audit.md. All 87 PNGs inspected in the 15 review-audit-contact sheets, with important frames opened individually.
Its one mechanical lead was the Flagged welcome interruption, confirmed and repaired. Sizes, mode/state layouts, Motion off, control/Enter paths, five-click checks, quick taps and resize stress otherwise passed.
The audit snapshot precedes the final compact-result, Read-catalog and modal-recovery repairs. Only affected states were re-shot afterward; no second full audit or polish round. Evidence: review-exit.log, review-exit-frames, review-compact-final.log and review-compact-final-frames in Scratch.
All 36 independent functional checks passed: exact bank/order/kind counts, every Practice length, 2-second green plus 2-second yellow thresholds, no automatic Practice advance, review subsets, skips, late Challenge input rejection and perfect scoring.
Bank recomputation: 114 + 50 + 36 = 200 unique lowercase entries. Smallest kind has 36 words, enough for a 30-word Challenge. A real 61-second wait ended Challenge; a keyboard-only 20-word run finished with focus on Again.
All eight STANDARDS sizes were checked, including the 375x812 iframe. Grayscale, Sound off with Read and Motion off were checked. Nominal contrast: ink/paper 12.06:1, muted/paper 5.82:1, white/blue 8.75:1, Right 6.90:1, Not yet 6.38:1.

| Voice check | Kind | Expected | Observed |
|---|---|---|---|
| Explore after five held Next taps, 2 s apart | welcome | 1 | 1 |
| Marking, review, Again and kind-guard Read hints | Read | 1 each | 1 each |
| Interrupted picker welcome after Close | welcome | 1 complete retry | 1 complete retry |
| Five perfect sessions | event | 5 complete cheers | 5 complete cheers |

Focused product checks had no console errors. The earlier phone host favicon 404 and a corrected test toggle-order assertion were harness issues, preserved in Scratch. The final hosted checks were clean.

#### Left open
- Owner bank approval, as the spec requires. Handoff preserves the builder's concerns and adds nog, fid, neg, dob and nesh as candidates for the owner's real-word/sound-alike review. No words were changed.
- Browser speech remains the spec-approved temporary voice. Muted Chrome verifies scheduling and text, not listening quality; no classroom trial was performed.
- Unattended decisions followed the owner's quiet Look and sibling direction over generic art/gameplay instructions. No questions, new topics, features or kit changes.
- Final report written last to honor the explicit stop instruction; the working draft was saved in Scratch throughout. No git commits. Drive cleanup completed; used ports are closed and temporary host.html is absent.
- System process inventory was denied by Windows. Browser cleanup used the prescribed drive.py routine; ports 9960, 9961 and 8765 were independently confirmed closed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: nonsense-words

#### Structure
src.html starts from the kit starter and inlines the supplied bank, grouped exactly as words.txt. CSS lays out the quiet parchment page, deep blue border, header modes, kinds, reading area and actions. The JavaScript owns deck order, marks, flags and deadline checks. Curio.voice owns instruction playback; kit Sound, Motion and Read are used directly.

The public __tool hook exposes state, setMode, allLines, vlog and vq for verification. state.started and state.wordStarted use performance.now(). tick runs every 100 ms and also checks visibility changes. Every score input independently checks the Challenge deadline.

#### Decisions and brief conflicts
- The owner's plain Look wins over the general rich-art/gameplay brief. Two assets only: quiet parchment and one small still quill. No people or characters; no motion or audio response to ordinary reading/scoring.
- First visit opens Explore. Later visits restore the remembered mode; Practice and Challenge stop at a ready screen until Start. This reconciles Explore opens first with remember last mode.
- The explicit instruction-only voice and prohibition on reading words win over generic K-2 narration of every fixed line. Browser voice is approved by the spec; six lines are prepared for voice night. Read never reads a target word.
- Metadata uses the spec's explicit driver students despite the generic K-2 teacher-driver contract. The notes and ready screens make the adult/partner support role clear.
- Practice and Challenge have a ready screen to avoid starting a clock while a teacher selects kinds or session length. Kinds and length are locked during a run; mode buttons can leave the run.
- No open-questions section is present. At least one kind stays selected; flags are per word and shown within current kinds, so overlapping mixes preserve flags. Best scores are per kind mix for comparable results.
- A Challenge timeout reports unreached words separately. Practice these covers attempted Not yet and skipped words, as specified. The denominator remains 30.
- Explore target words appear one at a time. The requested flagged picker and end-screen lists intentionally contain multiple words. They never speak the words.

#### Bank for owner approval
The bank is preserved without additions, removals or spelling changes. The number check found exactly 200 unique entries and the specified group counts. Owner review is still needed before shipping.
- vape is a real modern English word, and fab is a familiar informal real word.
- nife is a sound-alike of knife, despite the bank's stated sound-alike filter.
- pam reads as the name Pam; names may or may not count for the owner's filter.
- fode: possible non-English rude-word concern, unverified during this build. It remains in the owner-supplied bank as instructed; flag for the owner's multilingual review.
- CVCe items ending in ge can invite soft-g versus hard-g interpretations; u can have more than one long-vowel reading. A reading partner should accept the taught plausible decoding. This tool supplies no pronunciation key.

#### Sibling layout
Sight Words had only spec.md and words.json when this build began. Its source and handoff appeared during verification and were read. Both tools now share the parchment/blue stationery pattern and palette, quill and title at upper left, Explore / Practice test / Challenge, Sound / Motion / Read, centered plain word, large scoring controls, flags and privacy footer. Compact landscape places this tool's navigation and secondary controls alongside one another. The sibling needs its separate list picker and overlap tag. Both tools made their own assets. No sight-words files were changed.

#### Art made
Built-in image_gen made parchment and quill. Prompts: art/prompts.json. Raw originals: art/raw/parchment.png and art/raw/quill.png. Final assets: art/parchment.webp and art/quill.webp. No redraws; no people. Each finished image was inspected. The quill is intentionally small and still.

#### Art still to paint
None.

#### Engine changes wanted
None.

#### Verification
See codex-report.md for completed checks, exact evidence and limitations. No git commits, no changes outside this tool and its Scratch directory, and no polish round.

#### Build verification repairs
The one mechanical audit found a compact-layout hit-area problem: the empty secondary-actions container covered Start after the landscape columns were widened for review controls. CSS now hides that container when every child is hidden. Real held-click checks cover Start and scoring at 680, 800 and 1000 widths, plus the compact results-to-review path and perfect run. Selected controls also keep white-on-blue contrast while hovered. The report distinguishes the original audit leads from these targeted repairs; no second full audit was run.

Closing a first-tap Flagged dialog now retries an unheard Explore welcome, once the reading controls are visible again. Re-tapping the current mode preserves the session and its instruction rather than resetting it or cutting speech. Targeted held-click checks cover both paths. The public setMode hook still intentionally resets for verification and internal transitions.

Rapid kind changes refresh the deck and hint without hushing a still-valid generic instruction. The audit's three quick-kind speech-cut leads were repaired this way. A six-tap held-click check toggled each kind off/on at 0.7-second gaps, restored all 200 words and logged one uninterrupted Explore instruction.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-03)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-03)
