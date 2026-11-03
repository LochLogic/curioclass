# Codex report: nonsense-words

## Built
Offline Explore, Practice test and Challenge, preserving the owner-supplied 200-word bank. Quiet parchment, blue outer border and one still quill follow the owner's Look decision. Flags, last mode, kinds and per-kind-mix best scores persist on device. No git commits, polish round or changes to sibling source files.

## Numbers check
PASS: 114 CVC + 50 CVCe + 36 letter-pair words = 200 unique entries. Embedded bank matches words.txt character-for-character and in order. Scratch/check_bank.py and numbers.json hold the independent check. Practice thresholds are 2,000 and 4,000 ms; Challenge cap is 60,000 ms. Thirty-word sessions always have enough entries, including the smallest kind of 36.

## Feel check
Best moment: finishing a mixed practice run and opening exactly its Not yet and skipped words in Explore. The 30-of-30 banner also feels earned, with a brief cheer and optional confetti.

Two flattest moments were the cramped compact hourglass/counter area and an end screen whose review was squeezed behind too many settings. The build now reserves the reading area, fixes explicit grid rows, and hides settings on results so score and review stay legible. Ordinary reading deliberately stays quiet and still.

Played the full Explore, mixed Practice, retry and Challenge paths, including a real keyboard-only 20-word run. This is a teacher-supported drill, not a game: the person listening supplies the feedback. Scratch/bar-comparison.jpg places its 1366 frame beside Snowy Mail Route. Both bar tools were bundled only in Scratch and opened. This tool is visibly plainer by the owner's explicit decision. No richness or gameplay was added to override that decision.

## Done when
- PASS: all three modes work. Functional checks cover every session length, scoring, skips, flags, review, shuffle and deadline rejection; real held clicks cover the compact repair. functional-results.json has 38 passing assertions.
- PASS: exactly words.txt, filtered by the three kinds toggles. Counts and group boundaries were verified independently and in Chrome.
- PASS: Practice never advances on its own. A real wait confirmed green initially, yellow after 2.1 seconds, red after 4.3 seconds, same word and index. Marking resets the hourglass immediately.
- PASS: far below 2 MB. Final bundle is approximately 69 KB, with 5.3 KiB of art and no recorded audio.

Additional evidence: a real 62-second Challenge check was running at 31 seconds and done at 62 seconds; late marks are independently rejected by the deadline check. Keyboard-only Tab, Enter and arrows finished a 20-word practice run with focus on Again. F, R and N handlers were checked too. localStorage persistence and blocked-storage fallback work. No target word is ever spoken by the tool.

## Wave lessons
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

## Audit leads
Completed once, exit 0, with 40 grouped leads. Evidence: Scratch/audit/audit.md. All 81 audit PNGs were inspected in audit-contact/sheet-00.jpg through sheet-14.jpg.

- Two flags-open keep-region leads: intentional. A native modal covers the reading area and its underlying hint. The modal has its own instructions, a visible Close button, keyboard Escape and focus containment. Frames confirm this at every size.
- Six practice-running leads: fixed. Three focus-loss and three hidden-control rows came from the empty compact secondary-controls container intercepting Start. It is now hidden whenever all its buttons are hidden. Held clicks at 680x425, 800x500 and 1000x625 start the run, advance two words and retain focus on Not yet.
- Fourteen practice-results leads: fixed by the same hit-area repair. The missed Start meant all ten following Not yet taps were on hidden controls, so results were never reached. A new real-input 10-word compact run reaches results and opens its exact review subset.
- Fourteen review-subset leads: fixed by the same repair. The missed Start caused ten skipped-input misses, a missed Practice these tap and two hidden keep regions. The targeted review path now reaches Explore with exactly ten review words; All is visible. Skip and review semantics also passed the functional checks.
- One first-tap Flagged welcome lead: the reading instruction is intentionally withheld while the modal is up. Closing the dialog now retries the unheard welcome. A fresh-profile held-click Flagged then Close check logged one spoken Explore instruction and returned focus to Flagged.
- Three quick-kind speech-cut leads: fixed. Kind changes refresh deck, counter and hint without hushing a still-valid generic instruction. A six-tap test toggled every kind off/on at 0.7-second gaps, then waited nine seconds. It logged one uninterrupted instruction and restored all 200 entries.

The audit's size checks, Motion off check, ordinary control/Enter paths, five-click checks and resize stress checks otherwise passed. No console exceptions were found. A selected-hover contrast repair and preservation of the current mode were also verified with targeted held input. Re-tapping a running Challenge preserved its first mark; rapid repeats of the Practice mode did not cut its invitation.

Some audit sections were captured before these repairs. The final bundle has targeted rechecks, not a second full audit. The audit's iframe host used its original snapshot. No polish round was started.

## Frames looked at
All screenshots in early-frames, sizes-frames, modes-frames, phones-frames, functional-frames, targeted-frames, results-fix-frames, timeout-retry-frames, post-audit-fixes-frames, voice-recovery-frames, mode-repeat-frames and kind-quick-frames were viewed individually or in labeled contact sheets. Both bar frames and bar-comparison.jpg were viewed. Standard sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe. Modes include ready, running, red hourglass, flags dialog, results, review, timeout, perfect, grayscale, keyboard and Motion off. Audit contact sheets enumerate the audit frames viewed.

## Art made
Two built-in image_gen images: art/parchment.webp and art/quill.webp, 5,450 bytes total (5.3 KiB). No redraws. Full prompts and house style are in art/prompts.json; raw originals are in art/raw. Finished art was inspected at final size. No people or characters. Browser voice uses 0 KB of recorded audio. Bundle bytes: 70,626 bytes (69.0 KiB).

## Art still to paint
None.

## Engine changes wanted
None. All repairs are in this tool's CSS and logic.

## Left open
- Owner approval of words.txt before shipping. The bank is unchanged; handoff.md lists possible real words, sound-alikes, a name and an unverified multilingual wording concern.
- Browser speech is allowed by the spec until voice night; no recordings or listening review were made. Muted Chrome checked speech scheduling only.
- The full audit was not rerun after the compact hit-area, selected-hover, dialog welcome recovery, current-mode preservation and quick-kind speech fixes. Targeted real-input checks verify the fixes; a cold review is next.
- No classroom trial was performed. No polish round was started.
- The first real-time test's result was sampled before its screenshot wait, so it was not treated as deadline proof. A second attempt hit CDP's 60-second request cap; the smaller split-wait retry succeeded. Early host favicon 404s were removed with an inline icon and the host recheck was clean.

All started Chrome instances and servers were closed. Temporary host.html was removed.
