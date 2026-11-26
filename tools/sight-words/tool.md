# Sight Words: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: sight-words

#### Built
- Built the offline single-file reading tool in the required checkout. Repository writes stayed in tools/sight-words and _scratch/sight-words.
- Picker, all 16 sets, Mix, Explore, Practice test, Challenge, flags, review and device-only persistence are implemented.
- Owner's plain Look governs: parchment, blue border, a still quill and one readable word. No polish round or git commit.

#### Numbers check
- PASS: independent check-content.py confirms Dolch 40/52/41/46/41/95; ten Fry hundreds; 315 Dolch entries, 1,000 Fry entries and 273 overlaps.
- PASS: union is 1,042 words. Browser traversal checked every word in each of the 16 sets and every tag, with zero mismatches (sets-tags.json).
- PASS: Practice is green at 0 and 3,999 ms, yellow at 4,000 and 7,999 ms, red at 8,000 and 20,000 ms. Index stays unchanged.
- PASS: real Challenge timeout occurred at 60,050.8 ms; a late Right was rejected in the separate boundary check. Cap is 30 words and 60 seconds.
- Contrast ratios: ink/paper 12.06:1; muted/paper 5.82:1; white/blue 8.75:1; Right 7.73:1; Not yet 6.87:1.

#### Feel check
- Played a complete ten-word Practice session using real R/N keys and a held Skip: six Right, three Not yet, one Skip. Practice these returned exactly four review words.
- Best moment: returning directly to the child's own four words with no timer or score. The perfect Challenge banner is a second, deliberately rare payoff.
- Flattest moment 1: an initial compact ready screen clipped its lower button. Shortened its copy and placed Start and Choose sets together; rechecked ready-final.png.
- Flattest moment 2: long supplied entries could crowd a phone beside the hourglass. Added word fitting that resets on resize; inspected the Santa Claus phone frame.
- Compared with both bundled bar tools, copied and bundled only in Scratch. feel-comparison.png places Sight Words beside Snowy Mail Route. It is intentionally plainer, as the owner's Look requires.
- This is a calm adult-supported drill, not a game. I would use it for a short reading session, not claim that it has ten minutes of independent game depth.

#### Done when
- PASS: every Dolch and Fry set loads at its exact supplied count; every displayed word and tag was traversed in the browser.
- PASS: 273 on_both words carry the correct other-list tag. Case is normalized only for matching; displayed spelling is unchanged.
- PASS: four-second green and four-second yellow Practice intervals, no automatic skip or pace sound; Right, Not yet and Skip advance immediately.
- PASS: Challenge follows the sibling's 30-word/60-second cap, forward human marking, Skip as Not yet, per-selection best and perfect-score banner/chime/confetti.
- PASS: 10/20/30/whole-set lengths checked, including a mixed 115-word whole selection. All three modes and review paths exercised.
- PASS: keyboard-only Tab/Enter/arrow path, real F/R/N keys, persistent picks/Mix/list/flags after reload, grayscale, Motion off and instruction-only Read.

#### Wave lessons
- Hint and voice: PASS. Hints change immediately, separate ready/running instructions, current hint is Read's source. Held clicks at a two-second pace logged one Explore welcome and one explicit Read, with no repeated navigation narration.
- Focus and layout: PASS in driven paths. No load focus, stable picker buttons, reserved hint height, preventScroll on intentional focus, boundary focus transferred to an enabled control.
- Sizes: PASS in the 28-frame full sweep plus 375-wide iframe states. Targets are 60 px. Main controls and hint remain in view.
- No giveaways: PASS for this format. Scores are explicitly human marked; tags identify list overlap and never claim to assess pronunciation.
- Honest numbers: PASS. Set counts, deduplication and human scoring are explained; no automatic speech assessment is claimed.
- Standards: PASS. RF.2.3f is practiced by reading aloud. Additional K/1 codes are confined to teacher notes. No family engine exists.
- Motion off: PASS. No idle animation. Celebration movement disappears while the one-minute deadline stays real.
- Short choices: PASS in picker frames; all six Dolch or ten Fry choices are visible, including phone.
- Resize mid-action: covered by audit, disposition below. No moving simulation or async redraw owns the word state.
- Welcome delay: PASS in held-click log; no welcomeAfter and no delayed welcome after navigation.
- Unknown state: N/A, there are no hidden clues or inferred knowledge states.
- One look, one meaning: PASS. Right and Not yet have symbols and words, and pace colors also have text.
- Badge truth: PASS. Flag and overlap tags checked against state and supplied data.
- Reversible hints: PASS in mode changes and flagged-dialog return; the current step owns the hint synchronously.
- No answer by copying: N/A, the child reads aloud and a human marks; there is no answer-choice puzzle.

#### Audit leads
- Completed one full audit: _scratch/sight-words/audit/audit.md, 65 frames, 13 raw leads. No audit rerun after repairs.
- Explore tag/Back overlap: FIXED. Compact stack spacing now leaves 5.81 px below the tag.
- Explore tag/Next overlap: FIXED by the same change; targeted Explore frame and geometry checked.
- Practice tag/Not yet overlap: FIXED; targeted Practice frame and 5.81 px gap checked.
- Challenge tag/Not yet overlap: FIXED; targeted Challenge frame and geometry checked.
- Challenge tag/Right overlap: FIXED by the same spacing repair.
- Perfect .result-actions keep-region clipping: FIXED. Compact results reserve space for the controls; 680 and 800 frames inspected.
- Perfect short scroll-panel choices and hidden focus: FIXED by the same results repair. Review also stays visible, including a scrollable 1,042-word list, with actions bottom at 367 px in a 425 px window.
- Flag-list hides Back: accepted, the open modal intentionally covers the inert background. Close and word choices are visible.
- Flag-list hides the overlap tag: accepted for the same modal reason; full frame and contact sheet inspected.
- Flag-list hides Next: accepted for the same modal reason; keyboard dismissal returns focus to Flagged.
- Explore quick-tap welcome cut: FIXED. Re-tapping the selected mode now leaves speech alone; real double-tap log has one spoken welcome and no cut.
- Practice quick-tap welcome cut: FIXED by the same guard; quick-practice.json verified.
- Challenge quick-tap welcome cut: FIXED by the same guard; quick-challenge.json verified.
- Audit size checks and held-click/Enter paths had no other leads. Resize stress finished with no exceptions or stuck controls.
- Additional focused checks fixed last-word hints after closing flags and confirmed celebration clears immediately on the next reading screen.

#### Frames looked at
- Both bar frames; all emitted early frames; all nine emitted functional check frames; phone-early frames; all 28 matrix frames; all 11 matrix-phone frames; real-deadline.png and feel-comparison.png.
- Final matrix sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900. Phone is 375x812 through the host on port 8785.
- All 65 audit frames were inspected in eleven labeled contact sheets; all sixteen focused follow-up frames were opened. Failed driver attempts emitted no usable frame.

#### Art made
- Two images made with built-in imagegen: parchment and flourish. Full prompts: art/prompts.json. No people or placeholders.
- Final WebP art 11.42 KB; bundled HTML 90.56 KB; recorded voice 0 KB, well below the 2 MB goal.
- No redraws. The flourish was rekeyed with spill removal, then inspected at final size. Sources credit OpenAI gpt-image.

#### Art still to paint
None.

#### Engine changes wanted
None.

#### Left open
- Browser speech scheduling was inspected in muted Chrome; no recorded narration or listening review. No live classroom trial.
- The sibling's source appeared mid-build. Its visual pattern and mode logic were read; no sibling files were edited.
- The initial guide read used the tool's default wait without an explicit shell deadline. All later commands used explicit bounded jobs or the Scratch timeout runner. No command hit its cap.
- The user's explicit stop-on-report instruction means this report was written last, overriding the guide's early-report step.
- Automatic audit discovery initially missed the custom mode nav, so its walk covered the picker/header. Explicit audit states covered every mode at every size. Added role group for future automatic discovery and verified all three ids with the audit selector. No second full audit was run.
- The full size sweep and raw audit predate the compact layout, repeated-mode and hint repairs. Twelve focused layout/state frames, three rapid-tap voice frames and one celebration-exit frame verify those repairs; all were inspected with zero driver errors.
- The nearest built neighbor, Contraction Crusher, had no handoff.md or refine.md. Its source was read; Biased Bot's handoff/refine supplied the review-pattern reference.
- All browsers and servers started for this build were closed. host.html is absent; profiles and evidence remain in Scratch.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: sight-words

#### Structure

src.html started from the kit starter. It embeds the existing words.json with the json token, unchanged. The source has parchment and blue-border CSS, picker, reader, ready screen, results, flagged dialog, then deck and timing logic. Curio.voice owns the instruction queue; Curio owns Sound, Motion, Read and the perfect-score chime. There is no family engine.

window.__tool exposes state, setMode, allLines, vlog, vq, pool, tick and data. Practice uses wordAt, Challenge uses startedAt, both from performance.now(). The interval is 80 ms, visibility changes check the clock, and every score input checks the Challenge deadline before accepting a mark. A resize remeasures the current word from its normal font size so long entries fit on phones without splitting.

The mode navigation carries role group so the mechanical audit can discover its buttons. That attribute was added after the single audit's initial discovery, so the completed audit's automatic walk covers the picker; explicit audit states and separate held-click checks cover each reading mode. See the report for this verification limit and the targeted compact-spacing repair.

#### Decisions and brief conflicts

- The owner's plain Look wins over the rich-art and gameplay brief. Parchment and one still quill are the only illustrations. There are no people or characters and no motion near the word. Normal navigation and scoring are quiet. The perfect Challenge is the only celebration.
- No Open questions section exists in this spec. No unresolved teaching question was invented.
- Nonsense Words initially had only spec.md and words.txt. Its source appeared during this build and was read along with handoff.md. Both tools use the same parchment/blue stationery pattern, palette, quill at upper left, mode and utility controls, centered plain word, large plain scoring controls, flags and privacy footer. Sight Words needs a separate picker and overlap tag. Its two images were generated within this chat; no sibling files were changed.
- The spec explicitly requests driver students, so metadata follows it despite generic K-2 teacher-driver wording. Notes and instructions make the adult/partner role clear.
- The explicit instructions-only voice wins over generic K-2 narration of every fixed line. The word, overlap tag and review words are never spoken. Browser speech is allowed by the spec. Eight short instruction lines cover picker, modes, ready screens, review and flags; no recordings were made.
- The picker is always the first screen, with remembered picks, list tab, Mix and mode. The clock starts only after Start on the ready screen. Re-tapping the current mode preserves the current session.
- Multiple picks can span Dolch and Fry. Duplicate words in a combined selection appear once; source label and tag use the first occurrence in the fixed Dolch-then-Fry set order. This preserves the supplied capitalization, including I and Santa Claus. A list-tab change leaves picks on the other tab selected, and the selected count reflects all picks.
- Practice and Challenge always shuffle; Mix controls shuffling across the combined Explore selection. Best scores are keyed by the exact sorted set combination. Flags are per word and shown within the current reading deck.
- Practice Skip is separate from Not yet internally, and both are in review. End also includes unread words so an early finish does not lose them. Challenge Skip counts as Not yet; unread timeout words also appear in review, clearly labeled as words left.
- One-word-at-a-time applies to the reading display. The required end review and flagged picker intentionally list several words.
- The report is written last because the user's explicit instruction says to stop as soon as codex-report.md is written. This takes precedence over the guide's early-report workflow.

#### Content and numbers

The supplied content is untouched. Dolch counts: 40, 52, 41, 46, 41 and 95. Fry has ten hundreds. There are 315 unique Dolch entries, 1,000 unique Fry entries, 273 shared entries, and 1,042 unique entries across all sets. The independent numbers script is in Scratch. Browser checks walked every supplied word and its tag with zero mismatches.

#### Art made

Built-in imagegen created both assets. Full prompts and house style are saved in art/prompts.json. Raw originals are art/raw/parchment.png and art/raw/flourish.png. Final files are art/parchment.webp and art/flourish.webp. The parchment is a quiet pale texture; the quill is small and still. The art.py rekey pipeline sized both assets and removed green spill from the flourish. No redraws or people. Finished assets were visually inspected.

#### Art still to paint

None.

#### Engine changes wanted

None.

#### Verification and next work

See codex-report.md for completed checks and audit dispositions. Scratch holds the scripts, frames and evidence. Browser speech was scheduler-tested with muted Chrome, not listening-reviewed. No classroom trial was performed. A cold review is next; no polish round or git commit was started here.


#### Final build verification

One full audit completed with 13 raw leads. Compact word/tag spacing, compact results visibility and repeated-mode speech interruption were repaired. Three modal-coverage leads were accepted with frame evidence. All 65 audit frames were inspected. The full size sweep and audit were not repeated after repairs; twelve focused layout/state frames, three rapid-tap voice frames and a celebration-exit frame were inspected instead. The final bundle exactly matches the checked final Scratch fixture. host.html is absent and the build's Chrome and server processes were closed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-03)
- 2026-11-25: handoff.md folded in (last changed 2026-11-03)
